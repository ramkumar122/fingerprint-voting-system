global county
county=0
def login1():
    vardhan.geometry("1000x650")
    def login():
        global var500
        un=var500.get()
        print("s"+un+"s")
        global var501
        ps=var501.get()
        print("s"+ps+"s")
        import psycopg2 as pg2
        con=pg2.connect(database='college',user='postgres',password=123)
        con.set_session(autocommit=True)
        cur=con.cursor()
        w="select * from login_info where faculty_name='%s'"%un   
        cur.execute(w,un)
        q=cur.fetchall()
        print(len(q))
        if(len(q)!=0):    
            if(ps==q[0][2]):
                print("Welcome")
                def get_result(): 
                    import psycopg2 as pg2
                    #vardhan=tk.Tk()
                    vardhan.title("SECVOTE")
                    #vardhan.geometry("1000x650")
                    vardhan.config(bg="light slate gray")
                    #vardhan.attributes('-fullscreen',True)
                    #vardhan.maxsize(1000,650)
                    global b1
                    
                    def scores():
                        global var60
                        
                        con=pg2.connect(database='college',user='postgres',password=123)
                        con.set_session(autocommit=True)
                        cur=con.cursor()
                        s=var60.get()
                        s=s.rstrip()
                        s=s.lstrip()
                        try:
                            s=int(s)
                            w="select * from voters where voter_id='%s';"%s
                            cur.execute(w,s)
                            q=cur.fetchall()
                            print(q,"arf")
                            if (len(q)!=0):
                                global voter_name
                                voter_name=q[0][1]
                                var1.set(q[0][1])
                                var2.set(q[0][4])
                                var3.set(q[0][2])
                                var4.set(q[0][3])
                                var5.set(q[0][5])
                                global voterid
                                voterid=s
                                global f200
                                f200.pack(side=tk.TOP,anchor="center",pady=10)
                                
                                cur1=con.cursor()
                                i=voterid
                                print(voterid,"mnb")
                                w="select * from voted_table where voter_id=%d"%i
                                print(w)
                                cur1.execute(w)
                                q1=cur1.fetchall()
                                print(q1)
                                cur1.close()
                                con.close()
                                
                                if q1[0][1]==None:
                                    try:
                                        global f7000
                                        global county
                                        if county==1:
                                            f7000.pack_forget()
                                            county=0
                                    except:
                                        pass
                                    global b200
                                    b200.pack(side=tk.LEFT,padx=5)
                                    
                                else:
                                    if county==0:
                                        b200.pack_forget()
                                        f7000=tk.Frame(vardhan)
                                        print("hello")
                                        l7000=tk.Label(f7000,text="Voter has already casted HIS/Her vote",font="italic 12 bold",bg="light slate gray",fg="white")
                                        l7000.pack(side=tk.LEFT,padx=5)
                                        f7000.pack()
                                        county=1
                                cur.close()
                                con.close()
                            else:
                                global l50
                                l50=tk.Label(f1,text="Voter ID is invalid",font="italic 12 bold",fg="white",bg="light slate gray")
                                l50.pack(side=tk.LEFT,padx=5,pady=5,anchor="center")
                                f200.pack_forget()
                                b1.pack_forget()
                                global b20
                                b20=tk.Button(f1,text="Ok",command=lambda:[l50.pack_forget(),b20.pack_forget(),b1.pack(side=tk.LEFT)],width=10)
                                b20.pack(side=tk.LEFT)
                        except Exception as e:
                            #global l50
                            print(e)
                            l50=tk.Label(f1,text="Voter ID is invalid",font="italic 12 bold",fg="white",bg="light slate gray")
                            l50.pack(side=tk.LEFT,padx=5,pady=5,anchor="center")
                            b1.pack_forget()
                            #global b20
                            b20=tk.Button(f1,text="Ok",command=lambda:[l50.pack_forget(),b20.pack_forget(),b1.pack(side=tk.LEFT)],width=10)
                            b20.pack(side=tk.LEFT)
                            
                    f100=tk.Frame(vardhan)
                    main_label=tk.Label(f100,text="Welcome to SecVote",font="italic 40 bold",fg="white",bg="steelblue4")
                    main_label.pack(pady=(14,0),padx=5)
                    f100.config(bg="steelblue4")
                    f100.pack(side=tk.TOP,anchor="w",pady=(0,10),fill=tk.X)
                    f1=tk.Frame(vardhan)
                    l1=tk.Label(f1,text="Enter VOTER ID:  ",font="italic 20 bold",fg="white",bg="light slate gray")
                    l1.pack(side=tk.LEFT,anchor="w",pady=5,padx=5)
                    global var60
                    global var60
                    var60=tk.StringVar()
                    var60.set("101")
                    e1=tk.Entry(f1,textvariable=var60)
                    e1.pack(side=tk.LEFT,anchor="w",padx=20,pady=10)
                    global b1
                    b1=tk.Button(f1,text="Enter",command=lambda:[scores()],width=5,height=0)
                    b1.pack(side=tk.LEFT,anchor="w",padx=10,pady=10)
                    f1.config(bg="light slate gray")
                    f1.pack(side=tk.TOP,anchor="w",fill=tk.X,padx=10,pady=5)
                    l2=tk.Label(vardhan,fg='white',bg="light slate gray",text="----------------------------------------------------------------------VOTER DETAILS-----------------------------------------------------------------",font="italic 14 bold")
                    l2.pack(pady=10)
            
                    f2=tk.Frame(vardhan)
                    l3=tk.Label(f2,text="Name                :",font="italic 20 bold",fg="white",bg="light slate gray")
                    l3.pack(side=tk.LEFT,anchor="w",padx=(200,0),pady=0)
                    global var1
                    var1=tk.StringVar()
                    e2=tk.Entry(f2,state=tk.DISABLED,textvariable=var1,width=50)
                    e2.pack(side=tk.LEFT,anchor="w",padx=12,pady=5)
                    f2.config(bg="light slate gray")
                    f2.pack(side=tk.TOP,anchor="w",pady=5)
                    f1000=tk.Frame(vardhan)
                    l4=tk.Label(f1000,text="Age                   :",font="italic 20 bold",fg="white",bg="light slate gray")
                    l4.pack(side=tk.LEFT,anchor="w",padx=(200,0),pady=5)
                    global var2
                    var2=tk.StringVar()
                    e3=tk.Entry(f1000,state=tk.DISABLED,textvariable=var2,width=50)
                    e3.pack(side=tk.LEFT,anchor="w",padx=12,pady=5)
                    f1000.config(bg="light slate gray")
                    f1000.pack(side=tk.TOP,anchor="w",pady=5)
                    
                    f3=tk.Frame(vardhan)
                    l6=tk.Label(f3,text="Father's Name  :",font="italic 20 bold",fg="white",bg="light slate gray")
                    l6.pack(side=tk.LEFT,anchor="w",padx=(200,0),pady=10)
                    global var3
                    var3=tk.StringVar()
                    e4=tk.Entry(f3,state=tk.DISABLED,textvariable=var3,width=50)
                    e4.pack(side=tk.LEFT,anchor="w",padx=10,pady=10)
                    
                    f3.config(bg="light slate gray")
                    f3.pack(side=tk.TOP,anchor="w",pady=5)

                    f4=tk.Frame(vardhan)
                    l8=tk.Label(f4,text="Sex                    :",font="italic 20 bold",fg="white",bg="light slate gray")
                    l8.pack(side=tk.LEFT,anchor="w",padx=(200,0),pady=10)
                    global var4
                    var4=tk.StringVar()
                    e6=tk.Entry(f4,state=tk.DISABLED,textvariable=var4,width=50)
                    e6.pack(side=tk.LEFT,anchor="w",padx=10,pady=10)
                    
                    f4.config(bg="light slate gray")
                    f4.pack(side=tk.TOP,anchor="w",pady=5)

                    f5=tk.Frame(vardhan)
                    l9=tk.Label(f5,text="Pin Code           :",font="italic 20 bold",fg="white",bg="light slate gray")
                    l9.pack(side=tk.LEFT,anchor="w",padx=(200,0),pady=10)
                    global var5
                    var5=tk.StringVar()
                    e8=tk.Entry(f5,state=tk.DISABLED,textvariable=var5,width=50)
                    e8.pack(side=tk.LEFT,anchor="w",padx=(10,0),pady=10)
                    
                    f5.config(bg="light slate gray")
                    f5.pack(side=tk.TOP,anchor="w",pady=5)
                    
                    def scan():
                        vardhan.geometry("1000x650")
                        f121=tk.Frame(vardhan)
                        main_label=tk.Label(f121,text="Welcome to SecVote",font="italic 40 bold",fg="white",bg="steelblue4")
                        main_label.pack(pady=(14,0),padx=5)
                        f121.config(bg="steelblue4")
                        f121.pack(side=tk.TOP,anchor="w",pady=(0,10),fill=tk.X)

                        global b600
                        b600=tk.Button(vardhan,text="<--Back",fg="white",width=10,bg="steelblue",command=lambda:[f602.pack_forget(),b600.pack_forget(),f121.pack_forget(),f100.pack(side=tk.TOP,anchor="w",pady=(0,10),fill=tk.X),f1.pack(side=tk.TOP,anchor="w",fill=tk.X,padx=10,pady=5),l2.pack(pady=10),f2.pack(side=tk.TOP,anchor="w",pady=5),f1000.pack(side=tk.TOP,anchor="w",pady=5),f3.pack(side=tk.TOP,anchor="w",pady=5),f4.pack(side=tk.TOP,anchor="w",pady=5),f5.pack(side=tk.TOP,anchor="w",pady=5)])
                        b600.pack(anchor="nw")

                        global f602
                        f602=tk.Frame(vardhan)
                        f600=tk.Frame(f602)
                        l601=tk.Label(f600,text="Voter ID               :",font="italic 15 bold",bg="steelblue",fg="white")
                        l601.pack(side=tk.LEFT,padx=10)
                        global var600
                        var600=tk.StringVar()
                        e600=tk.Entry(f600,state=tk.DISABLED,textvariable=var600)
                        e600.pack(side=tk.LEFT,padx=10)
                        global voter_name
                        var600.set(voterid)
                        f600.config(bg="steelblue")
                        f600.pack(side=tk.TOP,anchor="nw",padx=10,pady=15)

                        global f601
                        f601=tk.Frame(f602)
                        l602=tk.Label(f601,text="Voter Name         :",font="italic 15 bold",bg="steelblue",fg="white")
                        l602.pack(side=tk.LEFT,padx=10)
                        global var601
                        var601=tk.StringVar()
                        e601=tk.Entry(f601,state=tk.DISABLED,textvariable=var601)
                        e601.pack(side=tk.LEFT,padx=10)
                        var601.set(voter_name)
                        f601.config(bg="steelblue")
                        f601.pack(side=tk.TOP,anchor="nw",padx=10,pady=15)

                        global f604
                        f604=tk.Frame(f602)
                        l604=tk.Label(f604,text="Voter Fingerprint :",font="italic 15 bold",bg="steelblue",fg="white")
                        l604.pack(side=tk.LEFT,padx=10)
                        global var604
                        var604=tk.StringVar()
                        e604=tk.Entry(f604,state=tk.DISABLED,textvariable=var604)
                        e604.pack(side=tk.LEFT,padx=10)
                        f604.config(bg="steelblue")
                        f604.pack(side=tk.TOP,anchor="nw",padx=10,pady=15)
                        
                        def fetch_and_display():
                            import tkinter
                            from tkinter import filedialog
                            global filename202
                            filename202=filedialog.askopenfilename(initialdir="C:/Users/Vardhan/Desktop/Test_Fingerprints")
                            var604.set(filename202)
                            global b6001
                            b6001.pack(side=tk.LEFT,padx=(20,0),pady=10)
                            print(filename202)
                        
                        def match():
                            try:
                                global filename202
                                print(filename202)
                                import os
                                a1=filename202.split("Test_Fingerprints/")
                                m1=a1[1].split("__")
                                path = "C:/Users/Vardhan/Desktop/SOCOFing/Real"
                                dir_list = os.listdir(path)
                                d={}
                                new_list=[]
                                global var60
                                print(var60.get(),"asdf",type(var60.get()))
                                g=var60.get()
                                g=int(g)
                                g=g-100
                                g=str(g)
                                print(g,"zxcv",type(g))
                                f=g
                                for i in dir_list:
                                    s=i.split("__")
                                    if s[0]==f:
                                        new_list.append(i)
                                print(new_list)
                                import os
                                import cv2
                                sample = cv2.imread(filename202)
                                best_score=0
                                filename=None
                                image=None
                                kp1,kp2,mp=None,None,None
                                counter=0
                                for file in new_list:
                                    print(file,filename202)
                                    if counter%10==0:
                                        print(file)
                                    counter+=1
                                    fingerprint_image=cv2.imread("C:/Users/Vardhan/Desktop/SOCOFing/Real/"+file)
                                    sift=cv2.SIFT_create()
                                    keypoints_1, descriptors_1=sift.detectAndCompute(sample,None)
                                    keypoints_2, descriptors_2=sift.detectAndCompute(fingerprint_image,None)
                                    matches=cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(descriptors_1,descriptors_2,k=2)
                                    match_points=[]
                                    for p,q in matches:
                                        if p.distance<0.1*q.distance:
                                            match_points.append(p)
                                    keypoints=0
                                    if len(keypoints_1)< len(keypoints_2):
                                        keypoints=len(keypoints_1)
                                    else:
                                        keypoints=len(keypoints_2)
                                    if len (match_points) / keypoints * 100 > best_score:
                                        best_score = len (match_points) / keypoints * 100
                                        filename = file
                                        image = fingerprint_image
                                        kp1,kp2,mp=keypoints_1,keypoints_2,match_points
                                print("BEST MATCH:"+ filename)
                                print("Score : "+str(best_score))

                                #result=cv2.drawMatches(sample,kp1,image,kp2,mp,None)
                                #result=cv2.resize(result,None,fx=4,fy=4)
                                #cv2.imshow("Result",result)
                                cv2.waitKey(0)
                                cv2.destroyAllWindows()
                                f2023=tk.Frame(f602)
                                main_label=tk.Label(f2023,text="Voter Fingerprints Matched Successfully. He/She Can Proceed to Vote.",font="italic 20 bold",fg="white",bg="steelblue4")
                                main_label.pack(pady=(0,0),padx=5)
                                f2023.config(bg="steelblue")
                                f2023.pack(side=tk.TOP,padx=10,pady=10)
                                b6000.pack_forget()
                                b6001.pack_forget()

                                import psycopg2 as pg2
                                con1=pg2.connect(database='college',user='postgres',password=123)
                                con1.set_session(autocommit=True)
                                cur2=con1.cursor()
                                global voterid
                                i=voterid
                                #w="select * from voted_table where voter_id=%d"%i
                                w="UPDATE voted_table SET voted = 1 WHERE voter_id=%d"%i
                                print(w)
                                cur2.execute(w)
                                cur2.close()
                                con1.close()
                            except Exception as e:
                                print(e)
                                f2023=tk.Frame(f602)
                                main_label=tk.Label(f2023,text="Voter Fingerprints did not Match.",font="italic 20 bold",fg="white",bg="steelblue4")
                                main_label.pack(pady=(0,0),padx=5)
                                f2023.config(bg="steelblue")
                                f2023.pack(side=tk.TOP,padx=10,pady=10)
                                b6000.pack_forget()
                                b6001.pack_forget()
   
                        f603=tk.Frame(f602)
                        b6000=tk.Button(f603,text="Upload",command=lambda:[fetch_and_display()],fg="white",bg="grey",width=8,font=1)
                        b6000.pack(side=tk.LEFT,pady=10)
                        global b6001
                        b6001=tk.Button(f603,text="Match",command=lambda:[match()],fg="white",bg="grey",width=8,font=1)
                        f603.config(bg="steelblue")
                        f603.pack(side=tk.TOP,padx=10,pady=10)
                        f602.config(bg="steelblue")
                        f602.pack(pady=40)

                    global f200
                    f200=tk.Frame(vardhan)
                    global b200
                    global f7000
                    try:
                        b200=tk.Button(f200,text="Scan",width=5,command=lambda:[f7000.pack_forget(),f200.pack_forget(),f5.pack_forget(),f4.pack_forget(),f3.pack_forget(),f100.pack_forget(),f1.pack_forget(),l2.pack_forget(),f2.pack_forget(),f1000.pack_forget(),scan()])
                        f200.config(bg="light slate gray")                    
                    except:
                        pass
                    vardhan.mainloop()
                get_result()
        
            else:
                print("hi")
                global l500
                l500.pack(fill=tk.X,pady=(0,15))
                global f502
                f502.pack(pady=40)
                l20=tk.Label(f501,text="Invalid Password",font="italic 12 bold",bg="light slate gray",fg="white")
                l20.pack(side=tk.LEFT,padx=5)
                b3=tk.Button(f501,text="Ok",width=5,command=lambda:[l20.pack_forget(),b3.pack_forget()])
                b3.pack(side=tk.LEFT,padx=5)

        if(len(q)==0):
            print("hi")
            #global l500
            l500.pack(fill=tk.X,pady=(0,15))
            #global f502
            f502.pack(pady=40)
            l21=tk.Label(f500,text="Invalid Username",font="italic 12 bold",bg="light slate gray",fg="white")
            l21.pack(side=tk.LEFT,padx=5)
            global b500
            b2=tk.Button(f500,text="Ok",width=5,command=lambda:[b500.pack(),l21.pack_forget(),b2.pack_forget()])
            b2.pack(side=tk.LEFT,padx=5)
        print(q)
        cur.close()
        con.close()
    global l500
    l500=tk.Label(vardhan,text="OPERATOR LOGIN",font="italic 30 bold",bg="steel blue",fg="white")
    l500.pack(fill=tk.X,pady=(0,15))
    global b500
    b500=tk.Button(vardhan,text="<--Back",fg="white",width=10,bg="steelblue",command=lambda:[b500.pack_forget(),l500.pack_forget(),f502.pack_forget(),l600.pack(pady=(250,0)),l601.pack(anchor="center",pady=10,padx=5),f20.pack(side=tk.TOP,pady=20)])
    b500.pack(anchor="nw")
    global f502
    f502=tk.Frame(vardhan)
    f500=tk.Frame(f502)
    l501=tk.Label(f500,text="Username:",font="italic 15 bold",bg="light slate gray",fg="white")
    l501.pack(side=tk.LEFT,padx=10)
    global var500
    var500=tk.StringVar()
    e500=tk.Entry(f500,textvariable=var500)
    e500.pack(side=tk.LEFT,padx=10)
    var500.set("vardhan")
    f500.config(bg="light slate gray")
    f500.pack(side=tk.TOP,anchor="nw",padx=10,pady=15)

    global f501
    f501=tk.Frame(f502)
    l502=tk.Label(f501,text="Password:",font="italic 15 bold",bg="light slate gray",fg="white")
    l502.pack(side=tk.LEFT,padx=10)
    global var501
    var501=tk.StringVar()
    e501=tk.Entry(f501,textvariable=var501,show="*")
    e501.pack(side=tk.LEFT,padx=10)
    var501.set("hello")
    f501.config(bg="light slate gray")
    f501.pack(side=tk.TOP,anchor="nw",padx=10,pady=15)

    f503=tk.Frame(f502)
    b1000=tk.Button(f503,text="Login",fg="white",bg="grey",command=lambda:[b500.pack_forget(),l500.pack_forget(),f502.pack_forget(),login()],width=8,font=1)
    b1000.pack(pady=10)
    f503.config(bg="light slate gray")
    f503.pack(side=tk.TOP,anchor="center",padx=10,pady=10)
    
    f502.config(bg="light slate gray")
    f502.pack(pady=40)
    vardhan.mainloop()

import tkinter as tk
vardhan=tk.Tk()
vardhan.title("SECVOTE")
vardhan.geometry("1000x650")
vardhan.config(bg="steelblue4")
l600=tk.Label(vardhan,text="Welcome to SECVOTE",fg="white",font="italic 50 bold",bg="steelblue4")
l600.pack(pady=(250,0),anchor="center")
l601=tk.Label(vardhan,text="                                                                                                                                     - A Secure way to VOTE",fg="orange",font="italic 12 bold",bg="steelblue4")
l601.pack(anchor="center",pady=10,padx=5)
f20=tk.Frame(vardhan,bg="steelblue4")
b22=tk.Button(f20,text="ADMIN LOGIN",fg="white",font=2,bg="grey")
b22.pack(side=tk.LEFT,padx=20)
b21=tk.Button(f20,text="OPERATOR LOGIN",fg="white",font=2,command=lambda:[f20.pack_forget(),l600.pack_forget(),l601.pack_forget(),login1()],bg="grey")
b21.pack(side=tk.LEFT,padx=10)

f20.pack(side=tk.TOP,pady=20)                                                                       
vardhan.mainloop()
