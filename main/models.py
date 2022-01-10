from django.db import models

#=====어드민 페이지를 위한 모델======
# 질문
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


    def __str__(self):
        return self.subject

# 답변
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()




#====특허 테이블 생성=====
#=====인공지능
class AiTest(models.Model):
    patent_name = models.CharField(max_length=100)
    patent_num = models.CharField(primary_key=True, max_length=100)
    patent_peo = models.CharField(max_length=50)
    up_num = models.CharField(max_length=20, blank=True, null=True)
    open_num = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_test'

#인공지능 개체명
class AiNer(models.Model):
    patent_num = models.CharField(max_length=100)
    ner_index = models.IntegerField(db_column='NER_index')  # Field name made lowercase.
    ner_word = models.CharField(db_column='NER_word', max_length=20)  # Field name made lowercase.
    ner = models.CharField(db_column='NER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ai_ner'


#=====의료,헬스
class MedicalTest(models.Model):
    patent_name = models.CharField(max_length=100)
    patent_num = models.CharField(primary_key=True, max_length=100)
    patent_peo = models.CharField(max_length=50)
    up_num = models.CharField(max_length=20, blank=True, null=True)
    open_num = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_test'

#의료, 헬스 개체명
class MedicalNer(models.Model):
    patent_num = models.CharField(max_length=100)
    ner_index = models.IntegerField(db_column='NER_index')  # Field name made lowercase.
    ner_word = models.CharField(db_column='NER_word', max_length=20)  # Field name made lowercase.
    ner = models.CharField(db_column='NER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medical_ner'


#=====자율주행
class SdTest(models.Model):
    patent_name = models.CharField(max_length=100)
    patent_num = models.CharField(primary_key=True, max_length=100)
    patent_peo = models.CharField(max_length=50)
    up_num = models.CharField(max_length=20, blank=True, null=True)
    open_num = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sd_test'

#자율주행 개체명
class SdNer(models.Model):
    patent_num = models.CharField(max_length=100)
    ner_index = models.IntegerField(db_column='NER_index')  # Field name made lowercase.
    ner_word = models.CharField(db_column='NER_word', max_length=20)  # Field name made lowercase.
    ner = models.CharField(db_column='NER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sd_ner'




#=====군사
class ArmyTest(models.Model):
    patent_name = models.CharField(max_length=100)
    patent_num = models.CharField(primary_key=True, max_length=100)
    patent_peo = models.CharField(max_length=50)
    up_num = models.CharField(max_length=20, blank=True, null=True)
    open_num = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'army_test'


#군사 개체명
class ArmyNer(models.Model):
    patent_num = models.CharField(max_length=100)
    ner_index = models.IntegerField(db_column='NER_index')  # Field name made lowercase.
    ner_word = models.CharField(db_column='NER_word', max_length=20)  # Field name made lowercase.
    ner = models.CharField(db_column='NER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'army_ner'
































#=====mysql DB=======
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)    
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainAnswer(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    question = models.ForeignKey('MainQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_answer'


class MainQuestion(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_question'