import datetime 
import os
import hashlib
class Date ():
    @staticmethod
    def Date_selection ():
        err=1
        while err==1:
            y=int(input('enter year in (****) format = ',))
            m=int(input('enter month in (**) format = ',)) 
            d=int(input('enter day in (**) format = ',))
            if y>=1000 and m>0 and d>0 and m<=12 and d<=31 and y<=9999:
                if m==2 and y%4==0 and d<=29:
                    if y%100==0:
                        if y%400==0:
                            da=f'{y}-{m}-{d}'
                            # dat=datetime.strptime(da,'%Y-%m-%d')
                            err=0
                        elif d<=28:
                            da=f'{y}-{m}-{d}'
                            # dat=datetime.strptime(da,'%Y-%m-%d')
                            err=0
                elif m==2 and y%4!=0 and d<=28:
                    da=f'{y}-{m}-{d}'
                    # dat=datetime.strptime(da,'%Y-%m-%d')
                    err=0
                elif m!=2 :
                    da=f'{y}-{m}-{d}'
                    # dat=datetime.strptime(da,'%Y-%m-%d')
                    err=0
            elif err==1:
                print('no date selected due to wrong input try again')
        return da
    @staticmethod
    def Current_Date ():
        datet = (datetime.datetime.now())
        dat = str(datet).split(' ')
        date = dat[0]
        return date
class india ():
    @staticmethod
    def State_selection():
        f=open('State_Data.txt','r')
        df=f.readlines()
        f.close()
        j =1
        for i in df:
            print(j," ",i)
            j+=1
        err=1
        while err==1:
            q=int(input('enetr index of state to select = ',))
            j=1
            for i in df :
                if j==q:
                    s=i
                    s=s.strip('\n')
                    err=0
                j+=1
            if err==1:
                print("wrong input/ invalid input try again")
        print()
        return s 
    @staticmethod
    def City_selection(s):
        f=open('City_Data/'+s+'.txt','r')
        df=f.readlines()
        f.close()
        j =1
        for i in df:
            print(j," ",i)
            j+=1
        err=1
        while err==1:
            q=int(input('enetr index of city to select = ',))
            j=1
            for i in df :
                if j==q:
                    p=i
                    p=p.strip('\n')
                    err=0
                j+=1
            if err==1:
                print("wrong input/ invalid input try again")
        print()
        return p  
class station():
    @staticmethod
    def station_add ():
        s=india.State_selection()
        p=india.City_selection(s)
        sn = str(input('enter station name = ',))
        # nt = int(input('enter number of platforms'))
        fs=open('Station_Data','a')
        fs.write(f"{sn}|{s}|{p}\n")
        fs.close()
    @staticmethod
    def check_station ():
        s=india.State_selection()
        p=india.City_selection(s)
        fs = open('Station_Data','r')
        ds=fs.readlines()
        fs.close()
        err=1
        for i in ds :
            dss = i.strip('\n').split('|')
            if dss[1]==s and dss[2]==p:
                print(i)
                err=0
        if err==1:
            print('any station at your city not found')
    @staticmethod
    def Station_selection_user():
        il=0
        while il==0:
            kli=1
            s=india.State_selection()
            p=india.City_selection(s)
            fs = open('Station_Data','r')
            ds=fs.readlines()
            fs.close()
            j=''
            for i in ds :
                dss = i.strip('\n').split('|')
                if dss[1]==s and dss[2]==p:
                    j+=f'{dss[0]},'
                    print(f'{kli} station in your place is {dss[0]}')
                    il=1
                    kli+=1
            err=1
            if il==1:
                while err==1:
                    print('enter the index of station you want to select')
                    ind = int(input())
                    jd=j.strip(',').split(',')
                    if ind>0 and ind<=len(jd):
                        print(f'{jd[ind-1]}')
                        final_stattion=f'{jd[ind-1]};{s};{p}'
                        err=0
                        return final_stattion
                    else :
                        print('wrong indexing try again')
            else:
                cker=0
                while cker!=2  and cker!=1:
                    print('there were no stations in city you selected if you want to select station at other city press 1 or else press 2')
                    cker=int(input())
                    if cker==2:
                        il=1
                        print('thank you')
                    elif cker==1:
                        il=0
                    else:
                        print('invalid input try again')
    @staticmethod
    def Station_selection_official ():
        il=0
        while il==0:
            kli=1
            s=india.State_selection()
            p=india.City_selection(s)
            fs = open('Station_Data','r')
            ds=fs.readlines()
            fs.close()
            j=''
            for i in ds :
                dss = i.strip('\n').split('|')
                if dss[1]==s and dss[2]==p:
                    j+=f'{dss[0]},'
                    print(f'{kli} station in your city is {dss[0]}')
                    il=1
                    kli+=1
            err=1
            if il==1:
                while err==1:
                    print('\nenter the index of station you want to select')
                    ind = int(input())
                    jd=j.strip(',').split(',')
                    if ind>0 and ind<=len(jd):
                        print(f'{jd[ind-1]}')
                        final_stattion=f'{jd[ind-1]}|{s}|{p}'
                        err=0
                        return final_stattion
                    else :
                        print('wrong indexing try again')
            else:
                print('there were no stations in city you selected')
class route():
    @staticmethod
    def get_filename(rout):
        return hashlib.md5(rout.encode()).hexdigest()
    @staticmethod
    def create_route():
        fr = open('Route_Data','a')
        x=int(input('enetr number of stations in total that the route will have = ',))
        print('choose staion one by one from where train will start to end to make a perfect route without any error\n\n')
        z=1
        frs=''
        xc=0
        rout=''
        while xc==0:
            while z<=x:
                print(f'choose station {z}\n\n')
                sta=station.Station_selection_official()
                if z!=x:
                    frs+=(f'{sta}:')
                    rout+=f'{sta}:'
                elif z==x:
                    frs+=(f'{sta}')
                    rout+=f'{sta}\n'
                z+=1
            xy=0
            while xy!=1 and xy!=2:
                print(f'final rout is \n{frs}\nif confirm press 1 if not press 2')
                xy = int(input())
                if xy==1:
                    fr.write(f'{frs}\n')
                    xc=1
                elif xy==2:
                    print('try creating whole route again')
                else:
                    print('invalid input')
        
        fr.close()
        rt=route.get_filename(rout)
        fff=open(f'Route_Train_Data/{rt}.txt','w')
        fff.close()
        {# fr=open('Route_Data','a')
        # frs=open('Station_Data','r')
        # x=int(input('enetr number of stations in total that the route will have'))
        # z=1
        # dr=frs.readlines()
        # print('choose staion one by one from where train will start to end to make a perfect route without any error thank you\n\n')
        # td=0
        # xc=0
        # while z<=x:
        #     xc=0
        #     print('select station {z}')
        #     s=india.State_selection()
        #     p=india.City_selection(s)
        #     mscn=0
        #     msc=''
        #     fsd=''
        #     for i in dr :
        #         ids=i.strip('\n').split(';')
        #         idss=i.strip('\n')
        #         if ids[1]==s and ids[2]==p:
        #             msc+=ids[0]+':'
        #             mscn+=1
        #             xc=1
        #             fsd+=idss+'*'
        #     if xc==0:
        #         print('wrong state or city try again')
        #     else:
        #         msc=msc.split(':')
        #         fsd=fsd.split('*')
        #         for i in range (0,mscn):
        #             print((i+1)," ", msc[i])
        #         print(f'above given are name of station in {s},{p} now enter index of staion you want to select')
        #         ind=0
        #         while (ind<=0 and ind>(mscn+1)):
        #             ind = int(input())
        #             print(f'confirm station {msc[ind-1]} if yes press 1 if no and want to enetr again press 2')
        #             a=0
        #             while a!=1 and x!=2:
        #                 a=int(input())
        #                 if a==1:
        #                     if z<x:
        #                         fr.write(f'{fsd[(ind-1)]}:')
        #                         td=1
        #                         z+=1
        #                     elif z==x:
        #                         fr.write(f'{fsd[(ind-1)]}')
        #                         td=1
        #                         z+=1
        #                 elif a==2:
        #                     print(f'try again adding station {z}')
        #                 else :
        #                     print("invalid input confirm again")
        # if td==1:
        #     fr.write('\n')
        # fr.close()
        # frs.close()
        }
    @staticmethod
    def route_selection_Official(): 
        xc=0
        while xc==0:
            print('given starting place')
            s1=india.State_selection()
            p1=india.City_selection(s1)
            print('ending place')
            s2=india.State_selection()
            p2=india.City_selection(s2)
            fr=open('Route_Data','r')
            dr=fr.readlines()
            fr.close()
            rn=1
            for i in dr :
                break_all=False
                # print(i)
                ds = i.strip('\n').split(':')
                # print(ds)
                for j in range (0,len(ds)):
                    xa = ds[j].split('|')
                    # print(xa)
                    if xa[1]==s1 and xa[2]==p1:
                        dss = i.strip('\n').split(':')
                        for l in range (j,len(dss)):
                            xaa = dss[l].split('|')
                            if xaa[1]==s2 and xaa[2]==p2:
                                xc=1
                                print(rn,' ',i)
                                inn = i.strip('\n')
                                isd += f'{inn}*'
                                rn+=1
                                break_all=True
                                break
                    if break_all:
                        break
            
            if xc==0:
                print('route not found try again')
            else:
                ind=0
                while ind==0:
                    print('enter index of route you want to select\n')
                    ind=int(input())
                    issd=isd.strip('*').split('*')
                    if ind<=len(issd) and ind>0:
                        issd[ind-1]+="\n"
                        # print(issd[ind-1])
                        return issd[ind-1]
                    else:
                        print('invalid input try again')
                        ind=0
    @staticmethod
    def route_selection_user():
        xc=0
        while xc==0:
            print('given starting place of your journey')
            s1=india.State_selection()
            p1=india.City_selection(s1)
            print('ending place of your journey ')
            s2=india.State_selection()
            p2=india.City_selection(s2)
            fr=open('Route_Data','r')
            dr=fr.readlines()
            fr.close()
            rn=1
            isd=''
            for i in dr :
                break_all=False
                ds = i.strip('\n').split(':')
                for j in range (0,len(ds)):
                    xa = ds[j].split('|')
                    if xa[1]==s1 and xa[2]==p1:
                        dss = i.strip('\n').split(':')
                        for l in range (j,len(dss)):
                            xaa = dss[l].split('|')
                            if xaa[1]==s2 and xaa[2]==p2:
                                xc=1
                                print(rn,' ',i)
                                inn=i.strip('\n')
                                isd += f'{inn}*'
                                rn+=1
                                break_all=True
                                break
                    if break_all:
                        break
            
            if xc==0:
                ex=0
                while ex!=1 and ex!=2:
                    print('direct route for your travel didnt found if you want to re try press 1 or if you want to exit press 2')
                    ex = int(input())
                    if ex==1:
                        xc=0
                    elif ex==2:
                        xc=1
                        return False
                    else:
                        print('invalid input')
                        ex=0
            else:
                ind=0
                while ind==0:
                    print('enter index of route you want to select\n')
                    ind=int(input())
                    issd=isd.strip('*').split('*')
                    # print(len(issd))
                    # print(isd)
                    if ind<=len(issd) and ind>0:
                        # print(issd[ind-1])
                        issd[ind-1]+='\n'
                        return issd[ind-1]
                    else:
                        print('invalid input try again')
                        ind=0
    @staticmethod
    def route_checker():
        print('given starting place of your journey')
        s1=india.State_selection()
        p1=india.City_selection(s1)
        print('ending place of your journey ')
        s2=india.State_selection()
        p2=india.City_selection(s2)
        fr=open('Route_Data','r')
        dr=fr.readlines()
        fr.close()
        xc=0
        rn=1
        for i in dr :
            break_all=False
            ds = i.strip('\n').split(':')
            for j in range (0,len(ds)):
                xa = ds[j].split('|')
                if xa[1]==s1 and xa[2]==p1:
                    dss = i.strip('\n').split(':')
                    for l in range (j,len(dss)):
                        xaa = dss[l].split('|')
                        if xaa[1]==s2 and xaa[2]==p2:
                            xc=1
                            print(rn,' ',i)
                            isd = f'{i}*'
                            rn+=1
                            break_all=True
                            break
                if break_all:
                    break
        
        if xc==0:
            print('direct route for your travel didnt found')
class Train():
    @staticmethod
    def Add_New_Train():
        tn = str(input('enetr name of train correctly',))
        tnu = int(input('enter train number',))
        x = int(input('number of 1A seats = ',))
        y = int(input('number of 2A seats = ',))
        z = int(input('number of 3A seats = ',))
        gen = int(input('Number of Non AC General seats = ',))
        f=open('Train_Data','a')
        f.write(f'{tnu};{tn};1A:{x};2A:{y};3A:{z};general:{gen}\n')
        f.close()
        tnnu=str(tnu)
        ff=open('Train_Full_Data/'+tnnu+'.txt','w')
        ff.write(f'Name = {tn}\nTrain Number = {tnu}\nNumber of 1st AC seats = {x}\nNumber of 2nd AC seats = {y}\nNumber of 3rd AC seats = {z}\nNumber of Non AC General seats = {gen}\nTotal_Journeys=0\n')
        ff.close()
        tfp=f'Train_Full_Data/{tnu}'
        os.makedirs(tfp, exist_ok=True)
    @staticmethod
    def add_route_to_train():
        err=1
        f=open('Train_Data','r')
        atd=f.readlines()
        f.close()
        rn = route.route_selection_Official()
        rnt=rn
        rn=rn.strip('\n')
        tnu=int(input('enter train number ',))
        nd = int(input('journey is of how many days = ',))
        print("select start date of journey")
        sd = Date.Date_selection()
        ssd=str(sd)
        # tdd=Date.Current_Date()
        er=0
        for i in atd :
            ds=i.strip('\n').split(';')
            if ds[0]==str(tnu):
                dss=i.strip('\n')
                dss+=f';{rn};Start_Date={ssd}'
                for j in range (2,nd+1):
                    if j!=(nd):
                        print(f'select date {j}')
                        ad=Date.Date_selection()
                        sad=str(ad)
                        dss+=f';Date_{j}={sad}'
                    else:
                        print(f'select End date {j}')
                        ad=Date.Date_selection()
                        sad=str(ad)
                        dss+=f';End_Date={sad}\n'
                        err=0
        if err==0:
            for x in range (0,(nd)):
                # print(dss)
                dsa = dss.strip('\n').split(';')
                # print(dsa)
                spdd=(dsa[7+x])
                spd=spdd.split('=')
                # print(spd)
                if os.path.exists(f'Dated_Train_Route_Data/{spd[1]}.txt'):
                    frs=open(f'Dated_Train_Route_Data/{spd[1]}.txt','r')
                else:
                    frs=open(f'Dated_Train_Route_Data/{spd[1]}.txt','w')
                    frs.close()
                    frs=open(f'Dated_Train_Route_Data/{spd[1]}.txt','r')
                dfrs=frs.readlines()
                frs.close()
                for cker in dfrs :
                    if cker.startswith(f'{tnu}'):
                        er=1
            if er==0:
                fr = open(f'Dated_Train_Route_Data/{ssd}.txt','a')
                fr.write(dss)
                fr.close()
                for x in range (1,(nd)):
                    dsa = dss.strip('\n').split(';')
                    spd=dsa[7+x].split('=')
                    frs=open(f'Dated_Train_Route_Data/{spd[1]}.txt','a')
                    frs.write(dss)
                    frs.close()
                ff=open('Train_Full_Data/'+str(tnu)+'.txt','r')
                tou=ff.readlines()
                ff.close()
                ff=open('Train_Full_Data/'+str(tnu)+'.txt','w')
                for jkl in tou:
                        jkul=jkl.strip('\n').split('=')
                        if jkul[0]=='Total_Journeys':
                            note=jkul[1]
                            num=int(note)
                            jkul[1]=(num+1)
                            ff.write(f'Total_Journeys={jkul[1]}\n')
                        else:
                            ff.write(jkl)
                        if jkl.startswith('Number of 1st AC seats'):
                            jkll=jkl.strip('\n')
                            xa=int(jkll.split('=')[1].strip())
                        if jkl.startswith('Number of 2nd AC seats'):
                            jkll=jkl.strip('\n')
                            ya=int(jkll.split('=')[1].strip())
                        if jkl.startswith('Number of 3rd AC seats'):
                            jkll=jkl.strip('\n')
                            za=int(jkll.split('=')[1].strip())
                        if jkl.startswith('Number of Non AC General seats'):
                            jkll=jkl.strip('\n')
                            gena=int(jkll.split('=')[1].strip())
                ff.close()
                ff=open('Train_Full_Data/'+str(tnu)+'.txt','a')
                ff.write(f'{num+1}~{dss}')
                ff.close()
                xp=int(input('Price of 1A seats',))
                yp=int(input('Price of 2A seats',))
                zp=int(input('Price of 3A seats',))
                genp=int(input('Price of Gen seats',))
                fff=open('Train_Full_Data/'+str(tnu)+'/'+str(num+1)+'.txt','w')
                # fff.write(f'1A(totle):{xa}\n1A(Price):{xp}\n1A(avl):{xa}\n1A(booked):0\n1A(bookedby):\n1A(waitlist):\n2A(totle):{ya}\n2A(Price):{yp}\n2A(avl):{ya}\n2A(booked):0\n2A(bookedby):\n2A(waitlist):\n3A(totle):{za}\n3A(Price):{zp}\n3A(avl):{za}\n3A(booked):0\n3A(bookedby):\n3A(waitlist):\ngen(totle):{gena}\ngen(Price):{genp}\ngen(avl):{gena}\ngen(booked):0\ngen(bookedby):\ngen(waitlist):\n')
                fff.write(f'1A(totle):{xa}\n1A(Price):{xp}\n1A(avl):{xa}\n1A(booked):0\n1A(bookedby):\n2A(totle):{ya}\n2A(Price):{yp}\n2A(avl):{ya}\n2A(booked):0\n2A(bookedby):\n3A(totle):{za}\n3A(Price):{zp}\n3A(avl):{za}\n3A(booked):0\n3A(bookedby):\ngen(totle):{gena}\ngen(Price):{genp}\ngen(avl):{gena}\ngen(booked):0\ngen(bookedby):\n')
                fff.close()
                rtn=route.get_filename(rnt)
                ffr=open(f'Route_Train_Data/{rtn}.txt','r')
                trs=ffr.readlines()
                ffr.close()
                nbl=0
                for ji in trs:
                    nbl+=1
                nbl+=1
                # rt=route.get_filename(str(rn))
                ffr=open(f'Route_Train_Data/{rtn}.txt','a')
                ffr.write(f'{nbl}~{dss}')
                ffr.close()
                print(f'train add to route {rnt} sucesfully')
            elif er==1:
                print('train number enetred already has a route for the particular date selected please verify records again')
                err=1        
        else :
            print('route adding failed try again with correct credenrials')
    @staticmethod
    def Edit_Train_Data():{


# # 2 have to made one which asks if train is to be edited for just one route or for all next incmonig routes


#         tn = str(input('enetr name of train correctly',))
#         tnu = int(input('enter train number',))
#         x = int(input('number of 1A seats',))
#         y = int(input('number of 2A seats',))
#         z = int(input('number of 3A seats',))
#         gen = int(input('Number of Non AC General seats',))
#         f=open('Train_Data','r')
#         drs=f.readlines()
#         f.close()
#         fr=open('Train_Data','w')
#         err=1
#         tdd=Date.Current_Date()
#         cd=tdd.split('-')
#         cy=cd[0]
#         cm=cd[1]
#         cday=[2]


# #here all files are to be made as clone and then delete at last but before delete cut copy paste into actual file of all condition meets 


#         for i in drs:
#             md = i.strip('\n').split(';')
#             if md[0]==tnu:
#                 fr.write(f'{tnu};{tn};1A:{x};2A:{y};3A:{z};general:{gen}\n')
#                 ff=open(f'Train_Full_Data/{tnu}.txt','r')
#                 dff=ff.readlines()
#                 ff.close()
#                 ff=open(f'Train_Full_Data/{tnu}.txt','w')
#                 err=0
#                 for jkl in dff:
#                     if jkl.startswith('Number of 1st AC seats'):
#                         jklm=jkl.strip('\n').split(' = ')
#                         jklm[1]=x
#                         ff.write(f'{jklm[0]} = {jklm[1]}\n')
#                     elif jkl.startswith('Number of 2nd AC seats'):
#                         jklm=jkl.strip('\n').split(' = ')
#                         jklm[1]=y
#                         ff.write(f'{jklm[0]} = {jklm[1]}\n')
#                     elif jkl.startswith('Number of 3rd AC seats'):
#                         jklm=jkl.strip('\n').split(' = ')
#                         jklm[1]=z
#                         ff.write(f'{jklm[0]} = {jklm[1]}\n')
#                     elif jkl.startswith('Number of Non AC General seats'):
#                         jklm=jkl.strip('\n').split(' = ')
#                         jklm[1]=gen
#                         ff.write(f'{jklm[0]} = {jklm[1]}\n')
#                     else:
#                         ff.write(jkl)
#                 ff.close()
#             else:
#                 fr.write(i)
#         if err==0:
#             ff=open(f'Train_Full_Data/{tnu}.txt','r')
#             dfr=ff.readlines()
#             ff.close()
#             for ij in dfr:
#                 if ij.startswith(int):
#                     ijl=ij.strip('\n').split(';')
#                     for ig in ijl:
#                         if ig.startswith('Start_Date'):
#                             igd=ig.split('=')
#                             fd=igd[1]
#                             fdd=fd.split('-')
#                             year=int(fdd[0])
#                             month=int(fdd[1])
#                             day=int(fdd[2])
#                     if year>=cy and month>=cm and day>cday:
#                         ffd=open(f'Train_Full_Data/{tnu}.txt','r')
#                         dr=ffd.readlines()
#                         ffd.close()
                        
# # here in train number.txt inside train full data updation of every jounery number there as number of seats written that is to be changed 

#                         jn=ijl[0]
#                         fff=open(f'Train_Full_Data/{str(tnu)}/{jn}.txt','r')
#                         df=fff.readlines()
#                         fff.close()
#                         fff=open(f'Train_Full_Data/{str(tnu)}/{jn}(clone).txt','w')
#                         for drf in df:
#                             if drf.startswith('1A(totle)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bx=int(dd[1])
#                                 fff.write(f'{dd[0]}:{x}\n')
#                             elif drf.startswith('2A(totle)'):
#                                 dd=drf.strip('\n').split(':')
#                                 by=int(dd[1])
#                                 fff.write(f'{dd[0]}:{y}\n')
#                             elif drf.startswith('3A(totle)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bz=int(dd[1])
#                                 fff.write(f'{dd[0]}:{z}\n')
#                             elif drf.startswith('gen(totle)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bgen=int(dd[1])
#                                 fff.write(f'{dd[0]}:{gen}\n')
#                             elif drf.startswith('1A(avl)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bavx=int(dd[1])
#                                 if x>bx:
#                                     ax=int(dd[1])
#                                     anx=((x-bx)+ax)
#                                     fff.write(f'{dd[0]}:{anx}\n')
#                                 elif(x==bx):
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif x<bx and (int(dd[1]))<x:
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif x<bx and (int(dd[1]))>x:
#                                     error=1
#                             elif drf.startswith('2A(avl)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bavy=int(dd[1])
#                                 if y>by:
#                                     ay=int(dd[1])
#                                     any=((y-by)+ay)
#                                     fff.write(f'{dd[0]}:{any}\n')
#                                 elif(y==by):
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif y<by and (int(dd[1]))<y:
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif y<by and (int(dd[1]))>y:
#                                     error=1
#                             elif drf.startswith('3A(avl)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bavz=int(dd[1])
#                                 if z>bz:
#                                     az=int(dd[1])
#                                     anz=((z-bz)+az)
#                                     fff.write(f'{dd[0]}:{anz}\n')
#                                 elif(z==bz):
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif z<bz and (int(dd[1]))<z:
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif z<bz and (int(dd[1]))>z:
#                                     error=1
#                             elif drf.startswith('gen(avl)'):
#                                 dd=drf.strip('\n').split(':')
#                                 bavgen=int(dd[1])
#                                 if gen>bgen:
#                                     agen=int(dd[1])
#                                     angen=((gen-bgen)+agen)
#                                     fff.write(f'{dd[0]}:{angen}\n')
#                                 elif(gen==bgen):
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif gen<bgen and (int(dd[1]))<gen:
#                                     fff.write(f'{dd[0]}:{dd[1]}\n')
#                                 elif gen<bgen and (int(dd[1]))>gen:
#                                     error=1
#                             else:
#                                 dd=drf.strip('\n').split(':')
#                                 fff.write(f'{dd[0]}:{dd[1]}\n')
#                         fff.close()
                

# # add error = 1 (means number of seats bokked are more and you have decreased number of seats) code when number of booked seates are greater than number of seates
                            
                                    
#         elif err==1:
#             print('train number might be wrong please try again with correct credentials')
#         fr.close()
    }
    @staticmethod
    def Search_Train():
        print('select route for which you want your train')
        rt=route.route_selection_user()
        if rt!=False:
            xrn=1
            rtn=route.get_filename(rt)
            ff=open(f'Route_Train_Data/{rtn}.txt','r')
            dfr=ff.readlines()
            ff.close()
            tdd=Date.Date_selection()
            cd=str(tdd).split('-')
            cy=int(cd[0])
            cm=int(cd[1])
            cday=int(cd[2])
            nbl=0
            njl=0
            for ij in dfr:
                asd=ij.split('~')
                if asd[0].isdigit():
                    ijl=ij.strip('\n').split(';')
                    for ig in ijl:
                        if ig.startswith('Start_Date'):
                            igd=ig.split('=')
                            fd=igd[1]
                            fdd=fd.split('-')
                            year=int(fdd[0])
                            month=int(fdd[1])
                            day=int(fdd[2])
                        if ig.startswith('End_Date'):
                            igd=ig.split('=')
                            fd=igd[1]
                            fdd=fd.split('-')
                            yeare=int(fdd[0])
                            monthe=int(fdd[1])
                            daye=int(fdd[2])
                    if (((year==cy)and(((month==cm) and (day>cday))or(month>cm))) or (year>cy)):
                                njl+=1
                                print(f'\n\nTrain {njl} found for date {day}/{month}/{year} to {daye}/{monthe}/{yeare}')
                                drs=ij.strip('\n').split('~')
                                tnu=int((drs[1].split(';'))[0])
                                tnn=((drs[1].split(';'))[1])
                                ff=open('Train_Full_Data/'+str(tnu)+'.txt','r')
                                kf=ff.readlines()
                                ff.close()
                                for i in kf:
                                    asd=i.split('~')
                                    if asd[0].isdigit():
                                        ik=i.strip('\n').split(';')
                                        for ikg in ik:
                                            if ikg.startswith('Start_Date'):
                                                ikgd=ikg.split('=')
                                                fkd=ikgd[1]
                                                fkdd=fkd.split('-')
                                                yr=int(fkdd[0])
                                                mnt=int(fkdd[1])
                                                dy=int(fkdd[2])
                                        if dy==day and mnt==month and yr==year:
                                            nbl=int((i.split('~'))[0])
                                            break
                                fff=open('Train_Full_Data/'+str(tnu)+'/'+str(nbl)+'.txt','r')
                                ijl=fff.readlines()
                                fff.close()
                                fiacpr=''
                                fiacseat=''
                                seacseat=''
                                seacpr=''
                                thacseat=''
                                thacpr=''
                                genseat=''
                                genacpr=''
                                for hy in ijl:
                                    hjy=hy.strip('\n').split(':')
                                    # print('1A price success')
                                    # print(hjy[0])
                                    # print(hjy[1])
                                    if hjy[0]=='1A(avl)':
                                        fiacseat=hjy[1]
                                    elif hjy[0]=='2A(avl)':
                                        seacseat=hjy[1]
                                    elif hjy[0]=='3A(avl)':
                                        thacseat=hjy[1]
                                    elif hjy[0]=='gen(avl)':
                                        genseat=hjy[1]
                                    elif hjy[0]=='1A(Price)':
                                        fiacpr=hjy[1]
                                    elif hjy[0]=='2A(Price)':
                                        seacpr=hjy[1]
                                    elif hjy[0]=='3A(Price)':
                                        thacpr=hjy[1]
                                    elif hjy[0]=='gen(Price)':
                                        genacpr=hjy[1]
                                    
                                print(f'Name = {tnn}\nTrain Number = {tnu}\nNumber of available 1st AC seats = {fiacseat}\nPrice of 1st AC seats = {fiacpr}\nNumber of availbale 2nd AC seats = {seacseat}\nPrice of 2nd AC seats = {seacpr}\nNumber of availble 3rd AC seats = {thacseat}\nPrice of 3rd AC seats = {thacpr}\nNumber of available General Non Ac seats = {genseat}\nPrice of General Non AC seats = {genacpr}')
                                xrn=0
            if xrn==1:
                print('Sorry no train found on the route you selected after any date for the date you selected')
    @staticmethod
    def Select_Train():
                print('select route for which you want your train')
                rt=route.route_selection_user()
                if rt!=False:
                    ps=0
                    rtn=route.get_filename(rt)
                    ff=open(f'Route_Train_Data/{rtn}.txt','r')
                    dfr=ff.readlines()
                    ff.close()
                    tdd=Date.Date_selection()
                    cd=str(tdd).split('-')
                    cy=int(cd[0])
                    cm=int(cd[1])
                    cday=int(cd[2])
                    nbl=0
                    njl=0
                    for ij in dfr:
                        asd=ij.split('~')
                        if asd[0].isdigit():
                            ijl=ij.strip('\n').split(';')
                            for ig in ijl:
                                if ig.startswith('Start_Date'):
                                    igd=ig.split('=')
                                    fd=igd[1]
                                    fdd=fd.split('-')
                                    year=int(fdd[0])
                                    month=int(fdd[1])
                                    day=int(fdd[2])
                                if ig.startswith('End_Date'):
                                    igd=ig.split('=')
                                    fd=igd[1]
                                    fdd=fd.split('-')
                                    yeare=int(fdd[0])
                                    monthe=int(fdd[1])
                                    daye=int(fdd[2])
                            if (((year==cy)and(((month==cm) and (day>cday))or(month>cm))) or (year>cy)):
                                        njl+=1
                                        print(f'\n\nTrain {njl} found for date {day}/{month}/{year} to {daye}/{monthe}/{yeare}')
                                        drs=ij.strip('\n').split('~')
                                        tnu=int((drs[1].split(';'))[0])
                                        tnn=((drs[1].split(';'))[1])
                                        ff=open('Train_Full_Data/'+str(tnu)+'.txt','r')
                                        kf=ff.readlines()
                                        ff.close()
                                        for i in kf:
                                            asd=i.split('~')
                                            if asd[0].isdigit():
                                                ik=i.strip('\n').split(';')
                                                for ikg in ik:
                                                    if ikg.startswith('Start_Date'):
                                                        ikgd=ikg.split('=')
                                                        fkd=ikgd[1]
                                                        fkdd=fkd.split('-')
                                                        yr=int(fkdd[0])
                                                        mnt=int(fkdd[1])
                                                        dy=int(fkdd[2])
                                                if dy==day and mnt==month and yr==year:
                                                    nbl=int((i.split('~'))[0])
                                                    break
                                        fff=open('Train_Full_Data/'+str(tnu)+'/'+str(nbl)+'.txt','r')
                                        ijl=fff.readlines()
                                        fff.close()
                                        fiacpr=''
                                        fiacseat=''
                                        seacseat=''
                                        seacpr=''
                                        thacseat=''
                                        thacpr=''
                                        genseat=''
                                        genacpr=''
                                        for hy in ijl:
                                            hjy=hy.strip('\n').split(':')
                                            if hjy[0]=='1A(avl)':
                                                fiacseat=hjy[1]
                                            elif hjy[0]=='2A(avl)':
                                                seacseat=hjy[1]
                                            elif hjy[0]=='3A(avl)':
                                                thacseat=hjy[1]
                                            elif hjy[0]=='gen(avl)':
                                                genseat=hjy[1]
                                            elif hjy[0]=='1A(Price)':
                                                fiacpr=hjy[1]
                                            elif hjy[0]=='2A(Price)':
                                                seacpr=hjy[1]
                                            elif hjy[0]=='3A(Price)':
                                                thacpr=hjy[1]
                                            elif hjy[0]=='gen(Price)':
                                                genacpr=hjy[1]
                                        print(f'Name = {tnn}\nTrain Number = {tnu}\nNumber of available 1st AC seats = {fiacseat}\nPrice of 1st AC seats = {fiacpr}\nNumber of availbale 2nd AC seats = {seacseat}\nPrice of 2nd AC seats = {seacpr}\nNumber of availble 3rd AC seats = {thacseat}\nPrice of 3rd AC seats = {thacpr}\nNumber of available General Non Ac seats = {genseat}\nPrice of General Non AC seats = {genacpr}')
                                        ps=1
                    if ps==1:
                        utn=0
                        while utn==0:
                            try:
                                print('Enter the index number of train you want to select ')
                                utn = int(input())
                            except ValueError:
                                utn = 0
                                print('Invalid input! Please type an integer number only.')
                                continue
                            if utn<=njl and utn>0:
                                ff=open(f'Route_Train_Data/{rtn}.txt','r')
                                dfr=ff.readlines()
                                ff.close()
                                nk=0
                                for ij in dfr:
                                    asd=ij.split('~')
                                    if asd[0].isdigit():
                                        ijl=ij.strip('\n').split(';')
                                        for ig in ijl:
                                            if ig.startswith('Start_Date'):
                                                igd=ig.split('=')
                                                fd=igd[1]
                                                fdd=fd.split('-')
                                                year=int(fdd[0])
                                                month=int(fdd[1])
                                                day=int(fdd[2])
                                        if (((year==cy)and(((month==cm) and (day>cday))or(month>cm))) or (year>cy)):
                                                    nk+=1
                                                    if nk==utn:
                                                        drs=ij.strip('\n').split('~')
                                                        tnu=int((drs[1].split(';'))[0])
                                                        tnn=((drs[1].split(';'))[1])
                                                        ff=open('Train_Full_Data/'+str(tnu)+'.txt','r')
                                                        kf=ff.readlines()
                                                        ff.close()
                                                        for i in kf:
                                                            asd=i.split('~')
                                                            if asd[0].isdigit():
                                                                ik=i.strip('\n').split(';')
                                                                for ikg in ik:
                                                                    if ikg.startswith('Start_Date'):
                                                                        ikgd=ikg.split('=')
                                                                        fkd=ikgd[1]
                                                                        fkdd=fkd.split('-')
                                                                        yr=int(fkdd[0])
                                                                        mnt=int(fkdd[1])
                                                                        dy=int(fkdd[2])
                                                                if dy==day and mnt==month and yr==year:
                                                                    nbl=int((i.split('~'))[0])
                                                                    return tnu,nbl
                                print('train selected')
                            else:
                                utn=0
                                print('index number you gave is incorrect please try again')
                    elif ps==0:
                        print('No Train Found for your Date on Route you Selected')
                        return 0,0
class user():
    def __init__(self):
        self.num=0     
    def Sign_Up_Log_In(self):
        log=0
        while log==0:
            print('1 for Log In and 2 for Sign Up ')
            log=int(input())
            if log == 2:
                ern=1
                while ern==1:
                    self.num=int(input('enter your mobile number = ',))
                    if len(str(self.num))==10:
                        ern=0
                    else:
                        print('not a 10 digit number')
                f=open('User_Ac_Rec','r')
                dr=f.readlines()
                f.close()
                for i in dr :
                    df=i.strip('\n').split(',')
                    if df[0]==f'{str(self.num)}':
                        print('account already exists please login there')
                        return False
                self.name=str(input('enter your name = ',))
                era=1
                while era==1:
                    self.age=int(input('enter your age = ',))
                    if self.age<=16:
                        print('sorry you cant sign up')
                        return False
                    else:
                        era=0
                erg=1
                while erg==1:
                    self.Gen=str(input('enetr M for male and F for female = ',))
                    if self.Gen=='f' or self.Gen=='F' or self.Gen=='Female' or self.Gen=='female' or self.Gen=='FEMALE':
                        Gen='Female'
                        erg=0
                    elif self.Gen=='m' or self.Gen=='M' or self.Gen=='Male' or self.Gen=='MALE' or self.Gen=='male':
                        self.Gen='Male'
                        erg=0
                    else:
                        print('not a correct option selected please select again')
                erad=1
                while erad==1:
                    print('enetr your 12 digit aadhar number or if you dont want to then please enter 2')
                    self.Aadhar=int(input())
                    if len(str(self.Aadhar))==12:
                        print('aadhar number saved successfully')
                        erad=0
                    elif self.Aadhar==2:
                        self.Aadhar=0
                        erad=0
                    else:
                        print('invalid input try again')
                erp=1
                while erp==1:
                    print('password should be of lenght 8-12 charachter')
                    self.password=str(input('set your password = ',))
                    if len(self.password)<=12 and len(self.password)>=8:
                        print('password set success')
                        erp=0
                    else:
                        print('please try setting password with 8-12 characters')
                f=open(f'User_Data/{self.num}.txt','w')
                f.write(f'Name = {self.name}\nAadhar Details = {self.Aadhar}\nmobile number = {self.num}\nAge = {self.age}\nGender = {self.Gen}\nTotal Bookings created = 0\n')
                f.close()
                ff=open('User_Ac_Rec','a')
                ff.write(f'{self.num},{self.password}\n')
                ff.close()
                print('Thank you your account has been created please login')
            elif log==1:
                err=2
                while err==2:
                    ern=1
                    while ern==1:
                        self.num=int(input('enter your mobile number = ',))
                        if len(str(self.num))==10:
                            ern=0
                        else:
                            print('not a 10 digit number')
                        err=3
                    while err==1 or err==3:
                        self.password=str(input('enter your password = ',))
                        ff=open('User_Ac_Rec','r')
                        dr=ff.readlines()
                        ff.close()
                        for i in dr:
                            df=i.strip('\n').split(',')
                            # print(df[0])
                            # print(type(df[1]),df[1])
                            # print(type(self.password),self.password)
                            if df[0]==str(self.num) and df[1]==(self.password):
                                err=0
                            elif df[0]==str(self.num):
                                err=1
                        if err==1:
                            print('wrong password try again')
                        elif err==3:
                            j=0
                            while j==0:
                                print('mobile number is not singed up please enter correct number or sing up\nto go back to main menu press 1 or if you want to try again press 2\n')
                                j = int(input())
                                if j==2:
                                    err=2
                                elif j==1:
                                    err=4
                                    log=0
                                else:
                                    print('try again invalid input')
                if err==0:
                    print('Thank You\nLog in success')
            else:
                log=0
                print("invalid input")
    def Search_station (self):
        print(station.check_station())
    def Search_Routes(self):
        print(route.route_checker())
    def Search_Train(self):
        print(Train.Search_Train())
    def Book_Train (self):
        self.tnu,self.jn=0,0
        nwb=0
        while self.tnu==0 and self.jn==0:
            self.tnu,self.jn=Train.Select_Train()
            self.tnu,self.jn=int(self.tnu),int(self.jn)
            if self.tnu!=0 and self.jn!=0:
                ss=0
                while ss==0:
                    print('Select which seat do you want :-\nPress 1 for 1st AC \nPress 2 for 2nd AC \nPress 3 for 3rd AC\nPress 4 for General Non AC seats')
                    ss=int(input())
                    if ss==1 :
                        sss='1A(avl)'
                        ssu='1st AC seat'
                        su='1A'
                    elif ss==2:
                        sss='2A(avl)'
                        ssu='2nd AC seat'
                        su='2A'
                    elif ss==3:
                        sss='3A(avl)'
                        ssu='3rd AC seat'
                        su='3A'
                    elif ss==4:
                        sss='gen(avl)'
                        su='gen'
                        ssu='General NON AC seat'
                    else:
                        ss=0
                        print('invalid input')
                f=open('Train_Full_Data/'+str(self.tnu)+'/'+str(self.jn)+'.txt','r')
                dr=f.readlines()
                f.close()
                for i in dr :
                    asd=i.strip('\n').split(':')
                    if asd[0] == sss:
                        nav=int(asd[1])
                        ns=0
                        while ns==0:
                            print('enter number of seats you want to book')
                            ns = int(input())
                            if ns<=0:
                                ns=0
                                print('invalid input try again')
                            elif ns<=nav:
                                print('Enter Details of Passengers correctly')
                                bd=f'{self.num}~{ns}~'
                                nmp=0
                                nfp=0
                                err=1
                                while err==1:
                                    print('number of Male passengers travelling are')
                                    nmp=int(input())
                                    if nmp<=ns and nmp>=0:
                                        nfp=ns-nmp
                                        for fp in range (0,nfp):
                                            Nm=str(input('Enter Name of Female Passenger = ',))
                                            ag=str(input('Enter Age of Female Passenger = ',))
                                            bd+=f'{Nm}-{ag};'
                                        for mp in range (0,nmp):
                                            Nm=str(input('Enter Name of male Passenger = ',))
                                            ag=str(input('Enter Age of male Passenger = ',))
                                            bd+=f'{Nm}-{ag};'
                                        bd=bd.strip(';')
                                        bd+='|'
                                        ff=open('Train_Full_Data/'+str(self.tnu)+'/'+str(self.jn)+'.txt','r')
                                        drs=ff.readlines()
                                        ff.close()
                                        for jk in drs:
                                            jk=jk.strip('\n')
                                            jkl=jk.split(':')
                                            if jkl[0]==(f'{su}(Price)'):
                                                sp=int(jkl[1])
                                                ba=ns*sp
                                                bp=0
                                                while bp==0:
                                                    print(f'Total Bill Amount is {ba} to pay press 1 or else to exit press 2')
                                                    bp=int(input())
                                                    if bp==1:
                                                        print('payment success')
                                                    elif bp==2:
                                                        nwb=1
                                                    else:
                                                        print('invalid input')
                                        if nwb!=1:
                                            ff=open('Train_Full_Data/'+str(self.tnu)+'/'+str(self.jn)+'.txt','w')
                                            for jk in drs:
                                                jkl=jk.strip('\n').split(':')
                                                if jkl[0]==(sss):
                                                    jkl[1]=f'{nav-ns}'
                                                    ff.write(f'{sss}:{jkl[1]}\n')
                                                elif jkl[0]==(f'{su}(bookedby)'):
                                                    ff.write(f'{jkl[0]}:{jkl[1]}{bd}\n')
                                                elif jkl[0]==(f'{su}(booked)'):
                                                    bs=int(jkl[1])
                                                    bs+=ns
                                                    ff.write(f'{jkl[0]}:{bs}\n')
                                                else:
                                                    ff.write(f'{jk}')
                                            ff.close()
                                            ubd=''
                                            ubdg=bd.strip('|').split('~')
                                            gubd=f'{ubdg[1]}~{ubdg[2]}'
                                            ubd+=f'number of {ssu} booked = {gubd}'
                                            fff=open(f'User_Data/{self.num}.txt','r')
                                            drf=fff.readlines()
                                            fff.close()
                                            for ij in drf :
                                                ijl=ij.strip('\n').split(' = ')
                                                if ijl[0]=='Total Bookings created':
                                                    tbc=int(ijl[1])
                                            non=int(tbc)+1
                                            fub=f'{non}:-{self.tnu}|{self.jn}|{ubd}'
                                            fff=open(f'User_Data/{self.num}.txt','w')
                                            for ij in drf:
                                                # print(ij)
                                                ijl=ij.strip('\n').split(' = ')
                                                if ijl[0]=='Total Bookings created':
                                                    ijl[1]=(tbc+1)
                                                    fff.write(f'{ijl[0]} = {ijl[1]}\n')
                                                else:
                                                    fff.write(ij)
                                            fff.write(f'{fub}\n')
                                            fff.close()
                                        err=0
                                        print('Booking success \nThank you')
                                    else:
                                        print('invalid input try again')
                                        err=1

                            elif ns > nav:
                                # print('enough seats are not available if you want we can put you at waitlist')
                                print(f'{ns} seats are not avaible in {ssu}')
            else:
                pbi=0
                while pbi==0:
                    print('do you want to try for another date as any train for that route after the date you selected is not available \nIf you want to retry Press 1\nIf you want to exit Press 2')
                    pbi=int(input())
                    if pbi==1:
                        print('select all credentials again')
                    elif pbi ==2:
                        self.tnu=1
                        self.jn=1
                        print('thank you')
                    else:
                        pbi=0
                        print('invalid input')
    def Check_Account_Detailes(self):
        f=open(f'User_Data/{self.num}.txt','r')
        drs=f.readlines()
        f.close()
        for i in drs:
            ij = i.strip('\n').split(' = ')
            if ij[0]=='Name' or ij[0]=='Aadhar Details' or ij[0]=='Age' or ij[0]=='Gender':
                print(i)
    def Check_Bookings(self):{
        # f=open(f'User_Data/{self.num}.txt','r')
        # drs=f.readlines()
        # f.close()
        # for i in drs:
        #     ij = i.strip('\n').split(' = ')
        #     if ij[0]!='Name' or ij[0]!='Aadhar Details' or ij[0]!='Age' or ij[0]!='Gender' or ij[0]!='Total Bookings created':
        #         ijl=i.strip('\n').split(':-')
                }
    def Change_Password(self):
        f=open('User_Ac_Rec','r')
        drs=f.readlines()
        f.close()
        f=open('User_Ac_Rec','w')
        for i in drs :
            if i.startswith(str(self.num)):
                erp=1
                while erp==1:
                    print('password should be of lenght 8-12 charachter')
                    self.password=str(input('set your password = ',))
                    if len(self.password)<=12 and len(self.password)>=8:
                        print('password set success')
                        erp=0
                    else:
                        print('please try setting password with 8-12 characters')
                ij=i.strip('\n').split(',')
                ij[1]=self.password()
                f.write(f'{ij[0],{ij[1]}}\n')
            else:
                f.write(i)
        f.close()
    def Change_Mob_Num(self):{
#         oldn=self.num
#         f=open('User_Ac_Rec','r')
#         drs=f.readlines()
#         f.close()
#         f=open('User_Ac_Rec','w')
#         for i in drs :
#             if i.startswith(str(self.num)):
#                 ij=i.strip('\n').split(',')
#                 ern=1
#                 while ern==1:
#                     self.num=int(input('enter your mobile number = ',))
#                     if len(str(self.num))==10:
#                         ern=0
#                     else:
#                         print('not a 10 digit number')
#                 ij[0]=self.num()
#                 erp=1
#                 while erp==1:
#                     print('password should be of lenght 8-12 charachter')
#                     self.password=str(input('set your password = ',))
#                     if len(self.password)<=12 and len(self.password)>=8:
#                         print('password set success')
#                         erp=0
#                     else:
#                         print('please try setting password with 8-12 characters')
#                 ij[1]=self.password()
#                 f.write(f'{ij[0],{ij[1]}}\n')
#                 ff=open(f'User_Data/{oldn}.txt','r')
#                 dr=ff.readlines()
#                 ff.close()
#                 os.remove(f'User_Data/{oldn}.txt')
#                 ff=open(f'User_Data/{self.num}.txt','w')
#                 for ik in dr:
#                     ff.write(ik)
#                 ff.close()
# # # change number in every trains booking page
#             else:
#                 f.write(i)
#         f.close()
        }
class Password():
    @staticmethod
    def passw(ps):
        psc=1
        if ps =='123':
            psc=0
            return psc
        else :
            return psc
class System_emp():
    @staticmethod
    def System_assces():
        ps=0
        er=0
        psc=1
        attemp=1
        while er==0 and attemp>0:
            print('enter password')
            ps=input()
            psc=Password.passw(ps)
            if psc==0:
                print('password confirmed you can continue')
                return psc
            else:
                attemp-=1
                print(f'incorrect password {attemp} attempts left')
def main():
    pb=0
    while pb==0:
        print('Press 1 to Log In/Sign Up\nPress 2 for Sys.emp')
        pb=int(input())
        if pb==1:
            us=user()
            us.Sign_Up_Log_In()
            fi=0
            while fi!=7:
                print('Press 1 to check for a Station\nPress 2 to check for a Route\nPress 3 to check for a Train\nPress 4 to Book Train Tickets\nPress 5 to Check Account Details\nPress 6 to Change Password\nPress 7 to Log Out')
                fi=int(input())
                if fi==1:
                    us.Search_station()
                elif fi==2:
                    us.Search_Routes()
                elif fi==3:
                    us.Search_Train()
                elif fi==4:
                    us.Book_Train()
                elif fi==7:
                    print('thank you')
                elif fi==5:
                    us.Check_Account_Detailes()
                elif fi==6:
                    us.Change_Password()
                else:
                    print('invalid input try again')

        elif pb==2:
            error=System_emp.System_assces()
            if error==0:
                pbs=0
                while pbs==0:
                    print('Press 1 to Add Station\nPress 2 to Create Route\nPress 3 to Add Train\nPress 4 to Add Route to Train')
                    pbs=int(input())
                    if pbs==1:
                        station.station_add()
                    elif pbs==2:
                        route.create_route()
                    elif pbs==3:
                        Train.Add_New_Train()
                    elif pbs==4:
                        Train.add_route_to_train()
                    else:
                        print('invalid input')
            else:
                return False
        else:
            print('invalid input try again')
            pb=0
main()