import time                                        #타이머용
from django.shortcuts import render                #파일 읽기
from django.http      import HttpResponse, request #html 코드로 제작가능
from django.db        import connection as conn    #DB 연동하여 쿼리 던지기위해 임포트
from .                import models as mo          #DB 연동을 위해 임폴트


#=====단순 반복코드=====
def datas_dic(datas) : #출원번호,요약문 출력코드
    space_list=[] #비어있는 리스트(리턴값)

    for data in datas :
        if len(data[1]) <10 : #내용없음 등의 특허들은 제거
            pass
        else :
            row ={"patent_num" :data[0], "text" : (data[1][:30]+"....")}
            space_list.append(row)

    return space_list




#=====페이지 기능 =====

def index(request): #메인페이지 연결
    template_name='mysite/index.html'

    category =request.GET.get("category")

    if category =="인공지능" :
        query =mo.AiTest.objects.all() #sql 쿼리를 모든 가져오기
        return render(request, template_name, {"query":query})
    
    elif category=="자율주행" :
        query =mo.SdTest.objects.all() #sql 쿼리를 모든 가져오기
        return render(request, template_name, {"query":query})
    
    elif category== "의료헬스" :
        query =mo.MedicalTest.objects.all() #sql 쿼리를 모든 가져오기
        return render(request, template_name, {"query":query})
    
    elif category== "군사" :
        query =mo.ArmyTest.objects.all() #sql 쿼리를 모든 가져오기
        return render(request, template_name, {"query":query})


    else :
        return render(request, template_name)
    


def wait(request) : #대기화면
    patent_num =request.GET.get("patent_num")
    return render(request, "mysite/wait.html",{"patent_num": patent_num})

    

    

def text_NER(request) :    #DB에서 요약문, 개체명 조회 후, 인덱스별 각인
    template_name="mysite/text_NER.html" #html 위치

    curs =conn.cursor()#DB연동
    

    # if category =="인공지능" :
    query ="""select patent_num, text from ai_test ORDER BY patent_num;""" #개체명,갯수 보여줘, 개체명으로 묶고, 갯수 정렬해
    curs.execute(query)#mysql 입력
    DB_datas =curs.fetchall()#지정 테이블 안의 모든 데이터를 추출
    conn.commit #DB 저장

    datas =datas_dic(DB_datas)
    patent_num =request.GET.get("patent_num")

    #요약문 개체명 섹션
    text= "==요약문을 클릭해주세요=="
    for db in DB_datas :
        if db[0]==patent_num :
            text= db[1]

    
    query_NER ="""select * from ai_ner  where patent_num='{}';""".format(patent_num) #
    curs.execute(query_NER)#mysql 입력
    NER_datas =curs.fetchall()#지정 테이블 안의 모든 데이터를 추출
    conn.commit #DB 저장

    ner =[]
    for ners in NER_datas :
        ner.append(ners[-2])

 



    return render(request, template_name, {"datas":datas, "text" :text, "ner" :ner})
    
    # elif category=="자율주행" :
    #     query =mo.SdTest.objects.all() #sql 쿼리를 모든 가져오기
    #     return render(request, template_name, {"query":query})
    
    # elif category== "의료헬스" :
    #     query =mo.MedicalTest.objects.all() #sql 쿼리를 모든 가져오기
    #     return render(request, template_name, {"query":query})
    
    # elif category== "군사" :
    #     query =mo.ArmyTest.objects.all() #sql 쿼리를 모든 가져오기
    #     return render(request, template_name, {"query":query})

    # else :
    #     query ="""select patent_num, text from ai_test ORDER BY patent_num;""" #개체명,갯수 보여줘, 개체명으로 묶고, 갯수 정렬해
    #     curs.execute(query)#mysql 입력
    #     datas =curs.fetchall()#지정 테이블 안의 모든 데이터를 추출
    #     conn.commit #DB 저장

    #     datas =datas_dic(datas)
    #     return render(request, template_name, {"datas":datas})