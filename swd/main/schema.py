import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import *

class UserType(DjangoObjectType):
    class Meta:
        model = User

class FacultyType(DjangoObjectType):
    class Meta:
        model = Faculty

class WardenType(DjangoObjectType):
    class Meta:
        model = Warden

class NucleusType(DjangoObjectType):
    class Meta:
        model = Nucleus

class SuperintendentType(DjangoObjectType):
    class Meta:
        model = Superintendent

class FacultyInchargeType(DjangoObjectType):
    class Meta:
        model = FacultyIncharge

class StaffType(DjangoObjectType):
    class Meta:
        model = Staff
   
class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class DayScholarType(DjangoObjectType):
    class Meta:
        model = DayScholar

class HostelPSType(DjangoObjectType):
    class Meta:
        model = HostelPS

class CSAType(DjangoObjectType):
    class Meta:
        model = CSA

class MessOptionType(DjangoObjectType):
    class Meta:
        model = MessOption
    
class BonafideType(DjangoObjectType):
    class Meta:
        model = Bonafide
    
class LeaveType(DjangoObjectType):
    class Meta:
        model = Leave

class DayPassType(DjangoObjectType):
    class Meta:
        model = DayPass

class LateComerType(DjangoObjectType):
    class Meta:
        model = LateComer

class InOutType(DjangoObjectType):
    class Meta:
        model = InOut

class DiscoType(DjangoObjectType):
    class Meta:
        model = Disco

class MessOptionOpenType(DjangoObjectType):
    class Meta:
        model = MessOptionOpen

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction

class MessBillType(DjangoObjectType):
    class Meta:
        model = MessBill


class Query(graphene.AbstractType):
    # used to get all data to the frontend
    current_user = graphene.Field(UserType)

    
    all_users = graphene.List(UserType)
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_facultys = graphene.List(FacultyType)
    faculty = graphene.Field(
        FacultyType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_wardens = graphene.List(WardenType)
    warden = graphene.Field(
        WardenType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_nucleuss = graphene.List(NucleusType)
    nucleus = graphene.Field(
        NucleusType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_superintedents = graphene.List(SuperintendentType)
    superintedent = graphene.Field(
        SuperintendentType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_faculty_incharges = graphene.List(FacultyInchargeType)
    facultyincharge = graphene.Field(
        FacultyInchargeType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_staffs = graphene.List(StaffType)
    staff = graphene.Field(
        StaffType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_students = graphene.List(StudentType)
    student = graphene.Field(
        StudentType,
        id=graphene.Int(),
        username = graphene.String(),
        name = graphene.String(),
        bitsId = graphene.String()
    )

    all_day_scholars = graphene.List(DayScholarType)
    day_scholar = graphene.Field(
        DayScholarType,
        id=graphene.Int(),
        username = graphene.String()
    )

    hostelps = graphene.Field(
        HostelPSType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_csas = graphene.List(CSAType)
    csa = graphene.Field(
        CSAType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_mess_options = graphene.List(MessOptionType)
    messoption = graphene.Field(
        MessOptionType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_bonafides = graphene.List(BonafideType)
    bonafide = graphene.Field(
        BonafideType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_leaves = graphene.List(LeaveType)
    leave = graphene.Field(
        LeaveType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_day_passs = graphene.List(DayPassType)
    daypass = graphene.Field(
        DayPassType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_late_comers = graphene.List(LateComerType)
    latecomer = graphene.Field(
        LateComerType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_in_outs = graphene.List(InOutType)
    inout = graphene.Field(
        InOutType,
        id=graphene.Int(),
        username = graphene.String()
    )
    
    all_discos = graphene.List(DiscoType)
    disco = graphene.Field(
        DiscoType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_mess_option_opens = graphene.List(MessOptionOpenType)
    messoptionopen = graphene.Field(
        MessOptionOpenType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_transactions = graphene.List(TransactionType)
    transaction = graphene.Field(
        TransactionType,
        id=graphene.Int(),
        username = graphene.String()
    )

    all_mess_bills = graphene.List(MessBillType)
    messbill = graphene.Field(
        MessBillType,
        id=graphene.Int(),
        username = graphene.String()
    )
    
    def resolve_current_user(self, args, **kwargs):
        if not context.user.is_authenticated():
            return None
        return context.user

    def resolve_all_users(self, args, **kwargs):
        return User.objects.all()

    def resolve_user(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return User.objects.get(id=id)

        if username is not None:
            return User.objects.get(username=username)

        return None

    def resolve_all_facultys(self, args, **kwargs):
        return Faculty.objects.all()

    def resolve_faculty(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Faculty.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            return Faculty.objects.get(user=user)

        return None

    def resolve_all_wardens(self, args, **kwargs):
        return Warden.objects.all()

    def resolve_warden(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Warden.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            faculty = Faculty.objects.get(user=user)
            return Warden.objects.get(faculty=faculty)

        return None

    def resolve_all_nucleuss(self, args, **kwargs):
        return Nucleus.objects.all()

    def resolve_nucleus(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Nucleus.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            faculty = Faculty.objects.get(user=user)
            return Nucleus.objects.get(faculty=faculty)

        return None

    def resolve_all_superintendents(self, args, **kwargs):
        return Superintendent.objects.all()

    def resolve_superintendent(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Superintendent.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            faculty = Faculty.objects.get(user=user)
            return Superintendent.objects.get(faculty=faculty)

        return None

    def resolve_all_faculty_incharges(self, args, **kwargs):
        return FacultyIncharge.objects.all()

    def resolve_facultyincharge(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return FacultyIncharge.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            faculty = Faculty.objects.get(user=user)
            return FacultyIncharge.objects.get(faculty=faculty)

        return None

    def resolve_all_staffs(self, args, **kwargs):
        return Staff.objects.all()

    def resolve_staff(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Staff.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            return Staff.objects.get(user=user)

        return None


    def resolve_all_students(self, args, **kwargs):
        return Student.objects.all()

    def resolve_student(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')
        name = kwargs.get('name')
        bitsId = kwargs.get('bitsId')


        if id is not None:
           return Student.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            return Student.objects.get(user=user)

        return None

    def resolve_all_day_scholars(self, args, **kwargs):
        return DayScholar.objects.all()

    def resolve_dayscholar(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return DayScholar.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return DayScholar.objects.get(student=student)

        return None
###

    def resolve_hostelps(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return HostelPS.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return HostelPS.objects.get(student=student)

        return None

    def resolve_all_csas(self, args, **kwargs):
        return CSA.objects.all()

    def resolve_csa(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return CSA.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return CSA.objects.get(student=student)

        return None

    def resolve_all_mess_options(self, args, **kwargs):
        return MessOption.objects.all()

    def resolve_messoption(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return MessOption.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return MessOption.objects.filter(student=student)

        return None

    def resolve_all_bonafides(self, args, **kwargs):
        return Bonafide.objects.all()

    def resolve_bonafide(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Bonafide.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return Bonafide.objects.filter(student=student)

        return None

    def resolve_all_leaves(self, args, **kwargs):
        return DayScholar.objects.all()

    def resolve_leave(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Leave.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return Leave.objects.filter(student=student)

        return None

    def resolve_all_day_passs(self, args, **kwargs):
        return DayPass.objects.all()

    def resolve_daypass(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return DayPass.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return DayPass.objects.filter(student=student)

        return None

    def resolve_all_late_comers(self, args, **kwargs):
        return LateComer.objects.all()

    def resolve_latecomer(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return LateComer.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return LateComer.objects.filter(student=student)

        return None

    def resolve_all_Discos(self, args, **kwargs):
        return Disco.objects.all()

    def resolve_disco(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Disco.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return Disco.objects.filter(student=student)

        return None

    def resolve_all_mess_option_opens(self, args, **kwargs):
        return MessOptionOpen.objects.all()

    def resolve_messoptionopen(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return MessOptionOpen.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return MessOptionOpen.objects.filter(student=student)

        return None

    def resolve_all_transactions(self, args, **kwargs):
        return Transaction.objects.all()

    def resolve_transaction(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return Transaction.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return Transaction.objects.filter(student=student)

        return None

    def resolve_all_mess_bills(self, args, **kwargs):
        return MessBill.objects.all()

    def resolve_messbill(self, args, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
           return MessBill.objects.get(id=id)

        if username is not None:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            return MessBill.objects.filter(student=student)

        return None


