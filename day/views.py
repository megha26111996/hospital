from django.shortcuts import render
from django.http import *
from .models import *
from django.core.files.storage import FileSystemStorage
from day import dbconnection
import random
def index(request):
    return render(request,'index.html',{})

def login(request):
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('password')
        sql="select * from adminlog where Username='"+str(a)+"' and Password='"+str(b)+"'"
        d=dbconnection.selectone(sql)
        if d:
            if d[3]=="admin":
                request.session['user']=a
                return HttpResponseRedirect('http://127.0.0.1:8000/admin')
            elif d[3]=="medicalofficer":
                request.session['user']=a
                return HttpResponseRedirect('http://127.0.0.1:8000/doc')
            elif d[3]=="receptionist":
                request.session['user']=a
                return HttpResponseRedirect('http://127.0.0.1:8000/pat')
        else:
            msg="User doesn't exist"
            return render(request,'login.html',{'msg':msg})    
    return render(request,'login.html',{})
def logout(request):
    return render(request,'index.html',{})    
def admin(request):
    return render(request,'admin.html',{})
def department(request):
    
    if request.method=="POST":
        a=request.POST.get('n1')
        b=request.POST.get('n2')
        sql="select * from dep where Department_ID='"+str(a)+"'"
        d=dbconnection.selectone(sql)
        sql1="select * from dep"
        p=dbconnection.selectall(sql1)
        if d:
            if a in d:
                msg="Department ID already exist"
                return render(request,'department.html',{"m":msg,"data":p})
        else:
            sql1="insert into dep(Department_ID,Department_Name) values('"+a+"','"+b+"')"
            dbconnection.insert(sql1)
            return HttpResponseRedirect('department')
    sql="select * from dep"
    data=dbconnection.selectall(sql)
    return render(request,'department.html',{"data":data})
def depupdate(request):
    uid=request.GET["id"]
    if request.method=="POST":
        a=request.POST.get("n1")
        b=request.POST.get("n2")
        sql2="update dep set Department_ID='"+a+"',Department_Name='"+b+"' where id='"+uid+"'"
        dbconnection.update(sql2)
        return HttpResponseRedirect("department")
    sql1="select * from dep where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    return render(request,'depupdate.html',{"data":o})
def depdel(request):
    did=request.GET["id"]
    sql="delete from dep where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("department")
       
def headdoc(request):
    if request.method=='POST':
        a=request.POST.get('n1')
        b=request.POST.get('n2')
        c=request.POST.get('n3')
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.FILES['n7']
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        sql1="insert into headdoc(Name,Username,Password,Qualification,Experience,Contact,Photo) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g.name+"')"
        sql2="insert into adminlog(Username,Password,U_type,U_status) values('"+b+"','"+c+"','medicalofficer',0)"
        dbconnection.insert(sql1)
        dbconnection.insert(sql2)
        return HttpResponseRedirect("headdoc")
    sql3="select * from headdoc"
    d=dbconnection.selectall(sql3)
    return render(request,'headdoc.html',{"data":d})
def headnur(request):
    if request.method=='POST':
        a=request.POST.get('n1')
        b=request.POST.get('n2')
        c=request.POST.get('n3')
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.FILES['n7']
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        sql1="insert into headnur(Name,Username,Password,Qualification,Experience,Contact,Photo) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g.name+"')"
        sql2="insert into adminlog(Username,Password,U_type,U_status) values('"+b+"','"+c+"','nursingofficer',0)"
        dbconnection.insert(sql1)
        dbconnection.insert(sql2)
        return HttpResponseRedirect("headnur")
    sql3="select * from headnur"
    d=dbconnection.selectall(sql3)
    return render(request,'headnur.html',{"data":d})
def rec(request):
    if request.method=='POST':
        a=request.POST.get('n1')
        b=random.randint(0,1000000)
        c=request.POST.get('n3')
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.POST.get('n7')
        h=request.FILES['n8']
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+h.name,h)
    
        # sql="select * from rec where Staff_ID='"+str(b)+"'"
        # d=dbconnection.selectone(sql)
        # sql1="select * from rec"
        # p=dbconnection.selectall(sql1)
        
        # if d:
        #     if b in d:
        #         msg="Staff ID already exist"
        #         return render(request,'rec.html',{"m":msg,"data":p})
        # else:
        sql1="insert into rec(Name,Staff_ID,Username,Password,Qualification,Experience,Contact,Photo) values('"+a+"','"+str(b)+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h.name+"')"
        sql2="insert into adminlog(Username,Password,U_type,U_status) values('"+c+"','"+d+"','receptionist',0)"
        dbconnection.insert(sql1)
        dbconnection.insert(sql2)
        return HttpResponseRedirect('rec')
    sql3="select * from rec"
    d=dbconnection.selectall(sql3)
    return render(request,'rec.html',{"data":d})
def doc(request):
    if request.method=='POST':
        a=request.POST.get('n1')
        b=request.POST.get('n2')
        c=request.POST.get('n3')
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.FILES['n7']
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        
        
        sql="select * from doc where Doctor_ID='"+str(b)+"'"
        d=dbconnection.selectone(sql)
        sql1="select * from doc"
        p=dbconnection.selectall(sql1)
        if d:
            if b in d:
                msg="Doctor ID already exist"
                return render(request,'doc.html',{"m":msg,"data":p})
        else:
            sql1="insert into doc(Name,Doctor_ID,Department,Qualification,Experience,Contact,Photo) values('"+a+"','"+str(b)+"','"+c+"','"+str(d)+"','"+e+"','"+f+"','"+g.name+"')"
            dbconnection.insert(sql1)
            return HttpResponseRedirect("doc")
            
    sql3="select * from doc"
    d=dbconnection.selectall(sql3)
    return render(request,'doc.html',{"data":d})
def pat(request):
    import datetime
    if request.method=='POST':
        a=request.POST.get('n1')
        b=random.randint(0,1000000)
        c=datetime.date.today()
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.POST.get('n7')
        
        
       
        
        sql1="insert into pat(Name,OP_number,Date,Doctor,Department,Address,Contact) values('"+a+"','"+str(b)+"','"+str(c)+"','"+str(d)+"','"+e+"','"+f+"','"+g+"')"
        dbconnection.insert(sql1)
        return HttpResponseRedirect("pat")
            
    sql4="select * from doc"       
    sql3="select * from pat"
    d=dbconnection.selectall(sql3)
    h=dbconnection.selectall(sql4)
    return render(request,'pat.html',{"data":d,"dat":h})

def headdocupdate(request):
    uid=request.GET["id"]
    if request.method=="POST":
        a=request.POST.get("n1")
        # b=request.POST.get("n2")
        # c=request.POST.get("n3")
        d=request.POST.get("n4")
        e=request.POST.get("n5")
        f=request.POST.get("n6")
        g=request.FILES["n7"]
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        sql2="update headdoc set Name='"+a+"',Qualification='"+d+"',Experience='"+e+"',Contact='"+f+"',Photo='"+g.name+"' where id='"+uid+"'"
       
        dbconnection.update(sql2)
        
        return HttpResponseRedirect("headdoc")
    sql1="select * from headdoc where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    return render(request,'headdocupdate.html',{"data":o})
def headdocdel(request):
    did=request.GET["id"]
    sql="delete from headdoc where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("headdoc")
    
def headnurupdate(request):
    uid=request.GET["id"]
    if request.method=="POST":
        a=request.POST.get("n1")
        # b=request.POST.get("n2")
        # c=request.POST.get("n3")
        d=request.POST.get("n4")
        e=request.POST.get("n5")
        f=request.POST.get("n6")
        g=request.FILES["n7"]
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        sql2="update headnur set Name='"+a+"',Qualification='"+d+"',Experience='"+e+"',Contact='"+f+"',Photo='"+g.name+"' where id='"+uid+"'"
        dbconnection.update(sql2)
        return HttpResponseRedirect("headnur")
    sql1="select * from headnur where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    return render(request,'headnurupdate.html',{"data":o})
def headnurdel(request):
    did=request.GET["id"]
    sql="delete from headnur where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("headnur")
    
def recupdate(request):
    uid=request.GET["id"]
    if request.method=="POST":
        a=request.POST.get("n1")
        # b=request.POST.get("n2")
        # c=request.POST.get("n3")
        # d=request.POST.get("n4")
        e=request.POST.get("n5")
        f=request.POST.get("n6")
        g=request.POST.get("n7")
        h=request.FILES["n8"]
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+h.name,h)
        sql2="update rec set Name='"+a+"',Qualification='"+e+"',Experience='"+f+"',Contact='"+g+"',Photo='"+h.name+"' where id='"+uid+"'"
       
        dbconnection.update(sql2)
       
        return HttpResponseRedirect("rec")
    sql1="select * from rec where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    return render(request,'recupdate.html',{"data":o})
def recdel(request):
    did=request.GET["id"]
    sql="delete from rec where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("rec")

def docupdate(request):
    uid=request.GET["id"]
    if request.method=="POST":
        a=request.POST.get("n1")
        b=request.POST.get("n2")
        c=request.POST.get("n3")
        d=request.POST.get("n4")
        e=request.POST.get("n5")
        f=request.POST.get("n6")
        g=request.FILES["n7"]
        fs=FileSystemStorage()
        fs.save("day/static/upload/"+g.name,g)
        sql2="update doc set Name='"+a+"',Doctor_ID='"+b+"',Department='"+c+"',Qualification='"+d+"',Experience='"+e+"',Contact='"+f+"',Photo='"+g.name+"' where id='"+uid+"'"
        dbconnection.update(sql2)
        return HttpResponseRedirect("doc")
    sql1="select * from doc where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    return render(request,'docupdate.html',{"data":o})
def docdel(request):
    did=request.GET["id"]
    sql="delete from doc where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("doc")

def patupdate(request):
    import datetime
    uid=request.GET["id"]
    if request.method=='POST':
        a=request.POST.get('n1')
        # b=request.POST.get('n2')
        c=datetime.date.today()
        d=request.POST.get('n4')
        e=request.POST.get('n5')
        f=request.POST.get('n6')
        g=request.POST.get('n7')
        sql2="update pat set Name='"+a+",Date='"+str(c)+"',Doctor='"+str(d)+"',Department='"+e+"',Address='"+f+"',Contact='"+g+"' where id='"+uid+"'"
        dbconnection.update(sql2)
        return HttpResponseRedirect("pat")
    sql1="select * from pat where id='"+uid+"'"
    o=dbconnection.selectone(sql1)
    sql="select * from doc"
    p=dbconnection.selectall(sql)
    return render(request,'patupdate.html',{"data":o,"dat":p})
def patdel(request):
    did=request.GET["id"]
    sql="delete from pat where id='"+did+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect("pat")

def docsearch(request):
    if request.method=="POST":
        a=request.POST.get("n1")
        sql="select *from doc where Name='"+a+"' or Department='"+a+"'"
        d=dbconnection.selectone(sql)
        if d:
            if d[1]==a:
                sql1="select *from doc where Name='"+a+"'"
                d=dbconnection.selectall(sql1)
                return render(request,'docsearch.html',{"data":d})
            elif d[3]==a:
                sql2="select *from doc where Department='"+a+"'"
                d=dbconnection.selectall(sql2)
                return render(request,'docsearch.html',{"data":d})
        else:
            msg="Doctor doesn't exist"
            return render(request,'docsearch.html',{"m":msg})
    
    return render(request,'docsearch.html',{})
def patview(request):
    sql="select * from pat"
    e=dbconnection.selectall(sql)
    return render(request,'patview.html',{'data':e})
def patsearch(request):
    if request.method=="POST":
        a=request.POST.get("n1")
        sql="select * from pat where OP_number='"+a+"' or Date='"+a+"'"
        d=dbconnection.selectone(sql)
        if d:
            if d[2]==a:
                sql1="select * from pat where OP_number='"+a+"'"
                d=dbconnection.selectall(sql1)
                return render(request,'patsearch.html',{"data":d})
            elif d[3]==a:
                sql2="select * from pat where Date='"+a+"'"
                d=dbconnection.selectall(sql2)
                return render(request,'patsearch.html',{"data":d})
        else:
            msg="Patient doesn't exist"
            return render(request,'patsearch.html',{"m":msg})
    return render(request,'patsearch.html',{})
def todaypat(request):
    import datetime
    cur_date=datetime.date.today()
    sql="select *from pat where date='"+str(cur_date)+"'"
    d=dbconnection.selectall(sql)
    return render(request,'todaypat.html',{"data":d})

def rectodaypat(request):
    import datetime
    cur_date=datetime.date.today()
    sql="select *from pat where date='"+str(cur_date)+"'"
    d=dbconnection.selectall(sql)
    return render(request,'rectodaypat.html',{"data":d})
def recpatsearch(request):
    if request.method=="POST":
        a=request.POST.get("n1")
        sql="select * from pat where OP_number='"+a+"' or Date='"+a+"'"
        d=dbconnection.selectone(sql)
        if d:
            if d[2]==a:
                sql1="select * from pat where OP_number='"+a+"'"
                d=dbconnection.selectall(sql1)
                return render(request,'recpatsearch.html',{"data":d})
            elif d[3]==a:
                sql2="select * from pat where Date='"+a+"'"
                d=dbconnection.selectall(sql2)
                return render(request,'recpatsearch.html',{"data":d})
        else:
            msg="Patient doesn't exist"
            return render(request,'recpatsearch.html',{"m":msg})
    return render(request,'recpatsearch.html',{})
    
    

# Create your views here.
