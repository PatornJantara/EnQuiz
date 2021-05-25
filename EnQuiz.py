from tkinter import *
import time
import os
import random


#===============================================================================================
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmm Engineering Quiz Game mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#===============================================================================================

class EnQuiz:

        def __init__(self,score):
                self.WinDlg = Tk()
                self.WinDlg.title("EnQuiz(EE)")
                self.score = score
                self.Mode = False

                self.ManageDlg()
#===============================================================================================

        def ManageDlg (self):
                self.Win_w = self.WinDlg.winfo_screenwidth()
                self.Win_h = self.WinDlg.winfo_screenheight()

                if self.Win_w > 1366 : self.Win_w = 1366
                if self.Win_h > 768  : self.Win_h = 768
                        
                self.WinDlg.geometry(str(self.Win_w)+"x"+str(self.Win_h))
               
                self.GameMode()


#===============================================================================================
        def GameMode(self):

                self.text = Label(self.WinDlg, text=" โปรแกรทจำลองสอบ กว " , font=("Helvetica", 36))
                self.text.place(x = self.Win_w/3 +100 ,y = (self.Win_h/2-300))

                self.text2 = Label(self.WinDlg, text="เกมจำลองข้อสอบ กว. เลือกโหมด 1 วิชาเดียว 2. จำลองการสอบจริง ",font=("Helvetica", 24))
                
                self.text2.place(x = self.Win_w/3 ,y = (self.Win_h/2-200))

                self.SingleMode = Button(self.WinDlg,text ="เลือกวิชาเดียว",font=("Helvetica", 36),command = self.ModeSetupSingleMode)
                self.RealMode   = Button(self.WinDlg,text ="จำลองการสอบจริง",font=("Helvetica", 36),command = self.RealTestMode)

                self.SingleMode.place(x = self.Win_w/3 +100 ,y = (self.Win_h/2-100) )
                self.RealMode.place(x = self.Win_w/3 +100,y = (self.Win_h/2) )

#==============================================================================================

        def ModeSetupSingleMode(self):

                self.text.after(0, self.text.destroy)
                self.text2.after(0, self.text2.destroy)
                self.SingleMode.after(0, self.SingleMode.destroy)
                self.RealMode.after(0, self.RealMode.destroy)

                self.SingleModeAns = 0
                
                self.SingleModeDlg()
                
#===============================================================================================
        def SingleModeDlg(self):
                self.text = Label(self.WinDlg, text=" เลือกวิชาทดสอบ " , font=("Helvetica", 28))
                self.text.place(x = self.Win_w/3 +100 ,y = 50)
                
                self.ComProMode = Button(self.WinDlg,text ="Computer Programming",font=("Helvetica", 16),command = self.GameDirCompro)
                self.EnDrawMode = Button(self.WinDlg,text ="Engineering Drawing",font=("Helvetica", 16),command = self.GameDirDrawing)
                self.StatMode = Button(self.WinDlg,text ="Static",font=("Helvetica", 16),command = self.GameDirStatic)
                self.MatMode = Button(self.WinDlg,text ="Engineering Material",font=("Helvetica", 16),command = self.GameDirMaterial)
                self.MachMode = Button(self.WinDlg,text ="Electrical Machines",font=("Helvetica", 16),command = self.GameDirMachine)
                self.DesignMode = Button(self.WinDlg,text ="Electrical System Design",font=("Helvetica", 16),command = self.GameDirDesign)
                self.PowerMode = Button(self.WinDlg,text ="Power System Analysis",font=("Helvetica", 16),command = self.GameDirPowerSys)

                

                self.ComProMode.place(x = self.Win_w/3 +100 ,y = 150 )
                self.EnDrawMode.place(x = self.Win_w/3 +100 ,y = 200 )
                self.StatMode.place(x = self.Win_w/3 +100 ,y = 250 )
                self.MatMode.place(x = self.Win_w/3 +100 ,y = 300 )
                self.MachMode.place(x = self.Win_w/3 +100 ,y = 350 )
                self.DesignMode.place(x = self.Win_w/3 +100 ,y = 400 )
                self.PowerMode.place(x = self.Win_w/3 +100 ,y = 450 )


#===============================================================================================
        def DestroySingleModeDlg(self):
                
                self.text.after(0, self.text.destroy)
                self.ComProMode.after(0, self.ComProMode.destroy)
                self.EnDrawMode.after(0, self.EnDrawMode.destroy)
                self.StatMode.after(0, self.StatMode.destroy)
                self.MatMode.after(0, self.MatMode.destroy)

                self.MachMode.after(0, self.MachMode.destroy)
                self.DesignMode.after(0, self.DesignMode.destroy)
                self.PowerMode.after(0, self.PowerMode.destroy)


#===============================================================================================
        
        def GameDirCompro(self):
                self.subject = 'compro'

                self.SetGameDir()
                self.SetQuestionNumber()
                
#===============================================================================================
                
        def SetGameDir(self):
                
                self.gamepath_org = os.getcwd()
                self.gamepath_org = self.gamepath_org +'\\'+ 'Question'


                if (self.Mode):
                        
                        for i in range (0,self.SubjectLen):
                                self.gamepath = self.gamepath_org +'\\'+self.SubjectList[i]+'\\'
                                self.QuestionRandLen[i] = len(os.listdir(self.gamepath))-1


                                file = open(self.gamepath_org + '\\'+self.SubjectList[i]+'\\' +self.SubjectList[i]+'_keyans.txt')
                                self.AnsKeyArr[i] = file.readlines()
                                file.close()

                        

                else :
                        self.gamepath = self.gamepath_org +'\\'+ self.subject + '\\'
                        file = open(self.gamepath + '\\'+self.subject +'_keyans.txt') 
                        self.KeyAns = file.readlines()
                        file.close()

#===============================================================================================
                
        def GameDirDrawing(self):

                self.subject = 'drawing'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================
        def GameDirStatic(self):
                     
                self.subject = 'static'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================
        def GameDirMaterial(self):
        
                self.subject = 'material'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================
        def GameDirMachine(self):

                self.subject = 'machine'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================
        def GameDirDesign(self):
                
                self.subject = 'design'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================
        def GameDirPowerSys(self):
                
                self.subject = 'powersys'
                self.SetGameDir()
                self.SetQuestionNumber()
#===============================================================================================

                
#===============================================================================================

        def SetQuestionNumber(self):

                self.DestroySingleModeDlg()
                
                self.text = Label(self.WinDlg, text=" เลือกจำนวนสุ่มข้อสอบ " , font=("Helvetica", 28))
                self.text.place(x = self.Win_w/3 + 50 ,y = 80)
                
                self.Easy_Q = Button(self.WinDlg,text ="50 ข้อ",font=("Helvetica", 16),command = self.SetQuestionNumber_Easy)
                self.Norm_Q = Button(self.WinDlg,text ="100 ข้อ",font=("Helvetica", 16),command = self.SetQuestionNumber_Norm)


                self.Easy_Q.place(x = self.Win_w/3 +100 ,y = 150 )
                self.Norm_Q.place(x = self.Win_w/3 +100 ,y = 200 )




#===============================================================================================
                
        def SetQuestionNumber_Easy(self):
                self.SetQuestNum = 50
                self.DestroySetQuestNum()
                
        def SetQuestionNumber_Norm(self):
                self.SetQuestNum = 100
                self.DestroySetQuestNum()
                
                
#==============================================================================================
        def DestroySetQuestNum(self):
                
                self.text.after(0, self.text.destroy)
                self.Easy_Q.after(0, self.Easy_Q.destroy)
                self.Norm_Q.after(0, self.Norm_Q.destroy)


                self.QuestionMatrice = ['o']*len(os.listdir(self.gamepath))
                self.QuestionLen = 0
                
                while True :
                        
                        RanQuestion = random.randint(1,len(os.listdir(self.gamepath))-1)
                        if len(os.listdir(self.gamepath+str( RanQuestion))) != 0 :
                               break
                
                self.ChoiceButton(RanQuestion)
                


#==============================================================================================

        def ChoiceButton(self,QuestionNum):

                b_Special = False
                
                image_size = [0,0]*5
                
                self.blJudge = True
                self.IsJugdePass = False
                
                self.QuestionLen = self.QuestionLen + 1
                
                self.QuestionNum = QuestionNum

                self.QuestionMatrice[QuestionNum-1] = 'x'

                self.ChoiceNum = len(os.listdir(self.gamepath + '\\'+ str(QuestionNum))) - 1
                
                self.SubjectName()

                self.SubjectStatus = Label(self.WinDlg, text =str(self.SubjectDisp) ,font=("Helvetica", 18))
                self.SubjectStatus.place(x = self.Win_w-300 ,y = 20)

                self.QuestionStatus = Label(self.WinDlg, text ="Question Number "+str(self.QuestionLen)
                                            +" / " + str(self.SetQuestNum),font=("Helvetica", 14))
                self.QuestionStatus.place(x = self.Win_w-300 ,y = 60)

                self.ScoreStatus = Label(self.WinDlg, text ="Score: "+str(self.score),font=("Helvetica", 30)
                                         ,foreground="sea green")
                self.ScoreStatus.place(x = self.Win_w-300 ,y = 200)


                self.Question_Img = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\q.PNG')

                
                self.Question = Label(self.WinDlg, image = self.Question_Img)                                 

                self.Img_1 = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\1.PNG')
                self.Img_2 = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\2.PNG')
                self.Img_3 = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\3.PNG')
                self.Img_4 = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\4.PNG')

                image_size[0] = self.Question_Img.height(),self.Question_Img.width()
                image_size[1] = self.Img_1.height(),self.Img_1.width()
                image_size[2] = self.Img_2.height(),self.Img_2.width()
                image_size[3] = self.Img_3.height(),self.Img_3.width()
                image_size[4] = self.Img_4.height(),self.Img_4.width()

                if (image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+image_size[4][0]+150 >= self.Win_h ):

                        b_Special = True

                if self.ChoiceNum == 5 :
                        self.Img_5 = PhotoImage(file= self.gamepath + '\\'+ str(QuestionNum) + '\\5.PNG')

                self.RadioBtn_1 = Button(self.WinDlg,command = self.ChangeQuestion_1    )
                self.RadioBtn_2 = Button(self.WinDlg,command = self.ChangeQuestion_2    )
                self.RadioBtn_3 = Button(self.WinDlg,command = self.ChangeQuestion_3    )
                self.RadioBtn_4 = Button(self.WinDlg,command = self.ChangeQuestion_4    )

                if self.ChoiceNum == 5 :
                        self.RadioBtn_5 = Button(self.WinDlg,command = self.ChangeQuestion_5)
                

                self.RadioBtn_1.config(image=self.Img_1)
                self.RadioBtn_2.config(image=self.Img_2)
                self.RadioBtn_3.config(image=self.Img_3)
                self.RadioBtn_4.config(image=self.Img_4)

                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.config(image=self.Img_5)


                if b_Special :
                        self.Question.place(x = 20 ,y = 20)
                        self.RadioBtn_1.place(x = 20 ,y = image_size[0][0]+30)
                        self.RadioBtn_2.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+40)
                        self.RadioBtn_3.place(x = 25 + image_size[1][1] ,y = image_size[0][0]+30)
                        self.RadioBtn_4.place(x = 25 + image_size[2][1] ,y = image_size[0][0]+image_size[3][0]+40)

                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.place(x = 30 + image_size[1][1] + image_size[3][1] ,y = image_size[0][0]+30)

                else:
                        self.Question.place(x = 20 ,y = 20)
                        self.RadioBtn_1.place(x = 20 ,y = image_size[0][0]+30)
                        self.RadioBtn_2.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+40)
                        self.RadioBtn_3.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+50)
                        self.RadioBtn_4.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+60)


                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+image_size[4][0]+70)

                self.NextQuest = Button(self.WinDlg,text ="NEXT",font=("Helvetica", 14),command = self.RandQuest,bg="blue",fg="white" )
                self.NextQuest.place(x = self.Win_w-300 ,y = 100)

                self.SummitQuest = Button(self.WinDlg,text ="SUMMIT ANSWER",font=("Helvetica", 14),
                                          command = self.JudgeAns,bg="springGreen4",fg="white" )
                
                self.SummitQuest.place(x = self.Win_w-220 ,y = 100)


#===============================================================================================

        def ChangeQuestion_1(self):
                if self.IsJugdePass == False:
                        self.SingleModeAns = 1

                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="medium aquamarine"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))

                
#=================================================================================================                
        def ChangeQuestion_2(self):
                if self.IsJugdePass == False:
                        self.SingleModeAns = 2

                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="medium aquamarine"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))

#=================================================================================================
                
        def ChangeQuestion_3(self):
                if self.IsJugdePass == False:
                        self.SingleModeAns = 3

                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="medium aquamarine"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))

                
#=================================================================================================
                
        def ChangeQuestion_4(self):
                if self.IsJugdePass == False:
                        self.SingleModeAns = 4

                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="medium aquamarine"))
                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))

#=================================================================================================  
        def ChangeQuestion_5(self):
                if self.IsJugdePass == False:
                        self.SingleModeAns = 5

                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="medium aquamarine"))
   
                        
#==============================================================================================================

        def RandQuest(self):

                if self.IsJugdePass == True :

                        self.SingleModeAns = 0
                
                        self.Question.after(0,self.Question.destroy)
                        self.RadioBtn_1.after(0, self.RadioBtn_1.destroy)
                        self.RadioBtn_2.after(0, self.RadioBtn_2.destroy)
                        self.RadioBtn_3.after(0, self.RadioBtn_3.destroy)
                        self.RadioBtn_4.after(0, self.RadioBtn_4.destroy)
                        if self.ChoiceNum == 5 :
                                 self.RadioBtn_5.after(0, self.RadioBtn_5.destroy)
                                 
                        self.NextQuest.after(0, self.NextQuest.destroy)
                        
                        self.SummitQuest.after(0, self.SummitQuest.destroy)
                
                        self.ScoreStatus.after(0, self.ScoreStatus.destroy)

                        self.SubjectStatus.after(0,  self.SubjectStatus.destroy)
                        self.QuestionStatus.after(0,  self.QuestionStatus.destroy)
                         
                        if (self.QuestionLen == self.SetQuestNum):
                                self.EndGame()
                        
                        blPass = False

                        while (blPass == False and self.QuestionLen != self.SetQuestNum):
                                
                                RanQuestion = random.randint(1,len(os.listdir(self.gamepath))-1)
                                if self.QuestionMatrice[RanQuestion-1] == 'o' and len(os.listdir(self.gamepath+str(RanQuestion))) != 0 :
                                        blPass = True
                                        self.ChoiceButton(RanQuestion)

#===========================================================================================================                

        def JudgeAns(self):

                if self.IsJugdePass == False and self.SingleModeAns != 0:
                        self.IsJugdePass = True
                        
                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                        
                        InTruAns = 0

                        InTruAns = int(self.KeyAns[self.QuestionNum-1])

                        if self.SingleModeAns == InTruAns and self.blJudge == True:
                                self.score += 1 

                                self.blJudge = False
                            
                                if self.SingleModeAns == 1 :
                                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="green"))
                                elif self.SingleModeAns == 2 :
                                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="green"))
                                elif self.SingleModeAns == 3 :
                                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="green"))
                                elif self.SingleModeAns == 4 :
                                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="green"))
                                elif self.SingleModeAns == 5 and self.ChoiceNum == 5 :
                                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="green"))

                        elif self.SingleModeAns != InTruAns and self.blJudge == True:

                                self.blJudge = False

                                if InTruAns == 1 :
                                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="green"))
                                elif InTruAns == 2 :
                                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="green"))
                                elif InTruAns == 3 :
                                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="green"))
                                elif InTruAns == 4 :
                                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="green"))
                                elif InTruAns == 5 and self.ChoiceNum == 5 :
                                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="green"))

                                if self.SingleModeAns == 1 :
                                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="red"))
                                elif self.SingleModeAns == 2 :
                                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="red"))
                                elif self.SingleModeAns == 3 :
                                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="red"))
                                elif self.SingleModeAns == 4 :
                                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="red"))
                                elif self.SingleModeAns == 5 and self.ChoiceNum == 5 :
                                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="red"))


                

#===========================================================================================================

        def EndGame(self):

                
                text = Label(self.WinDlg, text=" Game End" , font=("Helvetica", 60))
                text.place(x = self.Win_w/3 ,y = self.Win_h/4)

                text2 = Label(self.WinDlg, text= "Your Score is " + str(self.score) + " / " + str(self.SetQuestNum)
                              +" ===> "+str(round(self.score*100/self.SetQuestNum))+" %", font=("Helvetica", 36))

                text2.place(x = self.Win_w/3-100 ,y = (self.Win_h/2) - 50)

                if round(self.score*100/self.SetQuestNum) >= 60 :
                        
                        strResult = "Passed"
                        DispColor = "green"
                        
                        
                else :
                        strResult = "Failed"
                        DispColor = "red"
                        

                text3 = Label(self.WinDlg, text= strResult , font=("Helvetica", 36),foreground=DispColor)
        
                text3.place(x = self.Win_w/2-80 ,y = (self.Win_h/2) + 50)


                
      
#===========================================================================================================

        def SubjectName(self):
                self.SubjectDisp = ""
                if self.subject =='compro':
                        self.SubjectDisp = "Computer Programming"
                elif self.subject =='drawing':
                        self.SubjectDisp = "Engineering Drawing"
                elif self.subject =='static':
                        self.SubjectDisp = "Statics and Dynamics"
                elif self.subject =='material':
                        self.SubjectDisp = "Engineering Material"
                elif self.subject =='machine':
                        self.SubjectDisp = "Electrical Machines"
                if self.subject =='design':
                        self.SubjectDisp = "Electrical Systems Design"
                if self.subject =='powersys':
                        self.SubjectDisp = "Electrical Power Systems"
                if self.subject =='highvolt':
                        self.SubjectDisp = "Hight Voltage Engineering"

#===========================================================================================================
#============================================#
#============ Real Test Mode =====================#
#============================================#
                        
        def RealTestMode(self):
                
                self.Mode = True

                self.text.after(0, self.text.destroy)
                self.text2.after(0, self.text2.destroy)
                self.SingleMode.after(0, self.SingleMode.destroy)
                self.RealMode.after(0, self.RealMode.destroy)

                self.text = Label(self.WinDlg, text=" เลือกหมวดวิชาสอบ " , font=("Helvetica", 40))
                self.text.place(x = self.Win_w/3 +100 ,y = (self.Win_h/2-200) )

                self.GenMode = Button(self.WinDlg,text ="วิชาทั่วไป",font=("Helvetica", 32),command = self.GeneralSubject)
                self.FieldMode   = Button(self.WinDlg,text ="วิชาเฉพาะ (ไฟฟ้า)",font=("Helvetica", 32),command = self.FieldSubject)

                self.GenMode.place(x = self.Win_w/3 +100 ,y = (self.Win_h/2-100) )
                self.FieldMode.place(x = self.Win_w/3 +100,y = (self.Win_h/2) )
                
#===========================================================================================================         
        def RealTestModeDestroy(self):

                self.text.after(0, self.text.destroy)
                self.GenMode.after(0, self.GenMode.destroy)
                self.FieldMode.after(0, self.FieldMode.destroy)

                self.RealModeNumQuest = 25

#===========================================================================================================
        def GeneralSubject(self):
                self.RealTestModeDestroy()
                self.SubjectList = ['compro','drawing','static','material']
                self.SubjectDisp = ["Computer Programming","Engineering Drawing","Static","Engineering Material"]

                self.AnsSave = [[0]*self.RealModeNumQuest,[0]*self.RealModeNumQuest,[0]*self.RealModeNumQuest,[0]*self.RealModeNumQuest]
                self.QuestionSave = [['o']*self.RealModeNumQuest]*4
                self.QuestionRandGet = [0]*4
                self.QuestionRandLen = [0]*4
                self.AnsKeyArr = [0]*4

                self.TestMode = False
                self.SubjectLen = 4
                
                self.SetGameDir()
                self.RandQuestReal()

                self.RealModeDir = self.SubjectList[0]
                self.QuestionArrNum = 1


                self.ChoiceButtonReal()  
                self.RealTestAuxWindow()
                self.RealTestAuxWindowUpdate()

#===========================================================================================================
        def FieldSubject(self):
                self.RealTestModeDestroy()
                self.SubjectList = ['machine','design','powersys']
                self.SubjectDisp = ["Electrical Machines","Electrical System Design","Power System Analysis"]

                self.AnsSave = [[0]*self.RealModeNumQuest,[0]*self.RealModeNumQuest,[0]*self.RealModeNumQuest]
                self.QuestionSave = [['o']*self.RealModeNumQuest]*3
                self.QuestionRandGet = [0]*3
                self.QuestionRandLen = [0]*3
                self.AnsKeyArr = [0]*3

                self.TestMode = True
                self.SubjectLen = 3
                
                self.SetGameDir()
                self.RandQuestReal()

                self.RealModeDir =  self.SubjectList[0]
                self.QuestionArrNum = 1

                self.ChoiceButtonReal()
                self.RealTestAuxWindow()
                self.RealTestAuxWindowUpdate()

#===========================================================================================================
        def RealModeSetDir1(self):
                self.RealModeDir =  self.SubjectList[0]
                self.QuestionArrNum = 1
                self.RealTestAuxWindowUpdate()
        def RealModeSetDir2(self):
                self.RealModeDir =  self.SubjectList[1]
                self.QuestionArrNum = 1
                self.RealTestAuxWindowUpdate()
        def RealModeSetDir3(self):
                self.RealModeDir =  self.SubjectList[2]
                self.QuestionArrNum = 1
                self.RealTestAuxWindowUpdate()
        def RealModeSetDir4(self):
                self.RealModeDir =  self.SubjectList[3]
                self.QuestionArrNum = 1
                self.RealTestAuxWindowUpdate()
#===========================================================================================================
        def SetQuestion1(self):
                self.QuestionArrNum = 1
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion2(self):
                self.QuestionArrNum = 2
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion3(self):
                self.QuestionArrNum = 3
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion4(self):
                self.QuestionArrNum = 4
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion5(self):
                self.QuestionArrNum = 5
                self.RealTestAuxWindowUpdate()

        def SetQuestion6(self):
                self.QuestionArrNum = 6
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion7(self):
                self.QuestionArrNum = 7
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion8(self):
                self.QuestionArrNum = 8
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion9(self):
                self.QuestionArrNum = 9
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion10(self):
                self.QuestionArrNum = 10
                self.RealTestAuxWindowUpdate()

        def SetQuestion11(self):
                self.QuestionArrNum = 11
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion12(self):
                self.QuestionArrNum = 12
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion13(self):
                self.QuestionArrNum = 13
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion14(self):
                self.QuestionArrNum = 14
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion15(self):
                self.QuestionArrNum = 15
                self.RealTestAuxWindowUpdate()

        def SetQuestion16(self):
                self.QuestionArrNum = 16
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion17(self):
                self.QuestionArrNum = 17
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion18(self):
                self.QuestionArrNum = 18
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion19(self):
                self.QuestionArrNum = 19
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion20(self):
                self.QuestionArrNum = 20
                self.RealTestAuxWindowUpdate()

        def SetQuestion21(self):
                self.QuestionArrNum = 21
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion22(self):
                self.QuestionArrNum = 22
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion23(self):
                self.QuestionArrNum = 23
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion24(self):
                self.QuestionArrNum = 24
                self.RealTestAuxWindowUpdate()
                
        def SetQuestion25(self):
                self.QuestionArrNum = 25
                self.RealTestAuxWindowUpdate()
                
#===========================================================================================================

        def SetColor(self):

                self.subject =  0
                
                if self.RealModeDir == self.SubjectList[0]:
                        self.subject =  0
                elif self.RealModeDir == self.SubjectList[1]:
                        self.subject =  1
                elif self.RealModeDir == self.SubjectList[2]:
                        self.subject =  2
                if self.TestMode == False :
                        if self.RealModeDir == self.SubjectList[3]:
                                self.subject =  3

                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                        
                if(self.AnsSave[self.subject][self.QuestionArrNum-1] == 1):
                        self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="CadetBlue1"))
                elif(self.AnsSave[self.subject][self.QuestionArrNum-1] == 2):
                        self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="CadetBlue1"))
                elif(self.AnsSave[self.subject][self.QuestionArrNum-1] == 3):
                        self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="CadetBlue1"))
                elif(self.AnsSave[self.subject][self.QuestionArrNum-1] == 4):
                        self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="CadetBlue1"))
                elif(self.AnsSave[self.subject][self.QuestionArrNum-1] == 5):
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="CadetBlue1"))
                        

#============================================================================================================
        def NextReal(self):
                if self.QuestionArrNum < self.RealModeNumQuest :
                        self.QuestionArrNum += 1
                else :
                        self.QuestionArrNum = 1
                        
                        if self.RealModeDir ==  self.SubjectList[0]:
                                self.RealModeDir =  self.SubjectList[1]
                        elif self.RealModeDir ==  self.SubjectList[1]:
                                self.RealModeDir =  self.SubjectList[2]
                        elif self.RealModeDir ==  self.SubjectList[2]:
                                self.RealModeDir =  self.SubjectList[3]
                        if self.TestMode == False :
                                if self.RealModeDir ==  self.SubjectList[3]:
                                        self.QuestionArrNum = self.RealModeNumQuest

                                
                self.RealTestAuxWindowUpdate()
        

#===========================================================================================================
        def RandQuestReal(self):
                
                blPass = False

                for i in range (0,self.SubjectLen):
                        
                        randomlist = []
                        for j in range(0,self.RealModeNumQuest):
                                if self.QuestionRandLen[i] == 0 : continue
                                else :
                                        n = random.randint(1,self.QuestionRandLen[i])
                                        randomlist.append(n)
                        self.QuestionRandGet[i] = randomlist

#===========================================================================================================
        def RealTestAuxWindow(self):

                

                self.SubjectStatus = Label(self.WinDlg, text =str(self.SubjectDisp[0]) ,font=("Helvetica", 18))
                self.SubjectStatus.place(x = self.Win_w-300 ,y = 20)

                self.QuestionNumStatus = Label(self.WinDlg, text ="Question Number "+ str(self.QuestionArrNum)+str(self.RealModeNumQuest) ,font=("Helvetica", 14))
                self.QuestionNumStatus.place(x = self.Win_w-300 ,y = 60)

                self.NextQuest = Button(self.WinDlg,text ="NEXT",font=("Helvetica", 16),bg="blue",fg="white" ,command = self.NextReal )
                self.NextQuest.place(x = self.Win_w-300 ,y = 100)
                
                self.SetSubject1 = Button(self.WinDlg,text = self.SubjectDisp[0],font=("Helvetica", 16),command = self.RealModeSetDir1)
                self.SetSubject1.place(x = self.Win_w-300 ,y = 200)
                self.SetSubject2 = Button(self.WinDlg,text = self.SubjectDisp[1],font=("Helvetica", 16),command = self.RealModeSetDir2)
                self.SetSubject2.place(x = self.Win_w-300 ,y = 250)
                self.SetSubject3 = Button(self.WinDlg,text = self.SubjectDisp[2],font=("Helvetica", 16),command = self.RealModeSetDir3)
                self.SetSubject3.place(x = self.Win_w-300 ,y = 300)

                if self.TestMode == False :
                        self.SetSubject4 = Button(self.WinDlg,text = self.SubjectDisp[3],font=("Helvetica", 16),command = self.RealModeSetDir4)
                        self.SetSubject4.place(x = self.Win_w-300 ,y = 350)

                self.QuestionStatus= [0]*self.RealModeNumQuest
                self.QuestionStatus[0] = Button(self.WinDlg,text = "1",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion1)
                self.QuestionStatus[0].place(x = self.Win_w-300 ,y = 450)
                self.QuestionStatus[1] = Button(self.WinDlg,text = "2",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion2)
                self.QuestionStatus[1].place(x = self.Win_w-275 ,y = 450)
                self.QuestionStatus[2] = Button(self.WinDlg,text = "3",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion3)
                self.QuestionStatus[2].place(x = self.Win_w-250 ,y = 450)
                self.QuestionStatus[3] = Button(self.WinDlg,text = "4",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion4)
                self.QuestionStatus[3].place(x = self.Win_w-225 ,y = 450)
                self.QuestionStatus[4] = Button(self.WinDlg,text = "5",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion5)
                self.QuestionStatus[4].place(x = self.Win_w-200 ,y = 450)

                self.QuestionStatus[5] = Button(self.WinDlg,text = "6",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion6)
                self.QuestionStatus[5].place(x = self.Win_w-175 ,y = 450)
                self.QuestionStatus[6] = Button(self.WinDlg,text = "7",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion7)
                self.QuestionStatus[6].place(x = self.Win_w-150 ,y = 450)
                self.QuestionStatus[7] = Button(self.WinDlg,text = "8",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion8)
                self.QuestionStatus[7].place(x = self.Win_w-125 ,y = 450)
                self.QuestionStatus[8] = Button(self.WinDlg,text = "9",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion9)
                self.QuestionStatus[8].place(x = self.Win_w-100 ,y = 450)
                self.QuestionStatus[9] = Button(self.WinDlg,text = "10",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion10)
                self.QuestionStatus[9].place(x = self.Win_w-75 ,y = 450)

                self.QuestionStatus[10] = Button(self.WinDlg,text = "11",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion11)
                self.QuestionStatus[10].place(x = self.Win_w-300 ,y = 490)
                self.QuestionStatus[11] = Button(self.WinDlg,text = "12",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion12)
                self.QuestionStatus[11].place(x = self.Win_w-275 ,y = 490)
                self.QuestionStatus[12] = Button(self.WinDlg,text = "13",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion13)
                self.QuestionStatus[12].place(x = self.Win_w-250 ,y = 490)
                self.QuestionStatus[13] = Button(self.WinDlg,text = "14",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion14)
                self.QuestionStatus[13].place(x = self.Win_w-225 ,y = 490)
                self.QuestionStatus[14] = Button(self.WinDlg,text = "15",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion15)
                self.QuestionStatus[14].place(x = self.Win_w-200 ,y = 490)

                self.QuestionStatus[15] = Button(self.WinDlg,text = "16",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion16)
                self.QuestionStatus[15].place(x = self.Win_w-175 ,y = 490)
                self.QuestionStatus[16] = Button(self.WinDlg,text = "17",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion17)
                self.QuestionStatus[16].place(x = self.Win_w-150 ,y = 490)
                self.QuestionStatus[17] = Button(self.WinDlg,text = "18",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion18)
                self.QuestionStatus[17].place(x = self.Win_w-125 ,y = 490)
                self.QuestionStatus[18] = Button(self.WinDlg,text = "19",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion19)
                self.QuestionStatus[18].place(x = self.Win_w-100 ,y = 490)
                self.QuestionStatus[19] = Button(self.WinDlg,text = "20",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion20)
                self.QuestionStatus[19].place(x = self.Win_w-75 ,y = 490)

                self.QuestionStatus[20] = Button(self.WinDlg,text = "21",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion21)
                self.QuestionStatus[20].place(x = self.Win_w-300 ,y = 530)
                self.QuestionStatus[21] = Button(self.WinDlg,text = "22",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion22)
                self.QuestionStatus[21].place(x = self.Win_w-275 ,y = 530)
                self.QuestionStatus[22] = Button(self.WinDlg,text = "23",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion23)
                self.QuestionStatus[22].place(x = self.Win_w-250 ,y = 530)
                self.QuestionStatus[23] = Button(self.WinDlg,text = "24",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion24)
                self.QuestionStatus[23].place(x = self.Win_w-225 ,y = 530)
                self.QuestionStatus[24] = Button(self.WinDlg,text = "25",font=("Helvetica", 10),height = 1, width = 1,command = self.SetQuestion25)
                self.QuestionStatus[24].place(x = self.Win_w-200 ,y = 530)


                self.SummitScore = Button(self.WinDlg,text = "SUMMIT ANSWER",font=("Helvetica", 16),bg="green",fg="white" ,command = self.RealModeEnd)
                self.SummitScore.place(x = self.Win_w-300 ,y = self.Win_h-150)

                
#===========================================================================================================
        def RealModeEnd(self):
                
                self.SubjectStatus.after(0,self.SubjectStatus.destroy)
                self.QuestionNumStatus.after(0,self.QuestionNumStatus.destroy)
                self.NextQuest.after(0,self.NextQuest.destroy)
                
                self.Question.after(0,self.Question.destroy)
                self.RadioBtn_1.after(0, self.RadioBtn_1.destroy)
                self.RadioBtn_2.after(0, self.RadioBtn_2.destroy)
                self.RadioBtn_3.after(0, self.RadioBtn_3.destroy)
                self.RadioBtn_4.after(0, self.RadioBtn_4.destroy)
                if self.ChoiceNum == 5 :
                         self.RadioBtn_5.after(0, self.RadioBtn_5.destroy)

                self.SetSubject1.after(0, self.SetSubject1.destroy)
                self.SetSubject2.after(0, self.SetSubject2.destroy)
                self.SetSubject3.after(0, self.SetSubject3.destroy)

                if self.TestMode == False :
                        self.SetSubject4.after(0, self.SetSubject4.destroy)

                self.SummitScore.after(0, self.SummitScore.destroy)


                for button in range (0,self.RealModeNumQuest):
                        self.QuestionStatus[button].after(0, self.QuestionStatus[button].destroy)
                        

                for subject in range (0,self.SubjectLen):
                        for anscheck in range (0,self.RealModeNumQuest):

                                if self.AnsSave[subject][anscheck] == int(self.AnsKeyArr[subject][self.QuestionRandGet[subject][anscheck]-1]) :
                                        self.score += 1

                print(self.score)

                text = Label(self.WinDlg, text=" Game End" , font=("Helvetica", 60))
                text.place(x = self.Win_w/3 ,y = self.Win_h/4)

                if self.TestMode == False :
                        text = Label(self.WinDlg, text= str(self.score) + "/100", font=("Helvetica", 60))
                        text.place(x = self.Win_w/3+100 ,y = self.Win_h/4+100)
                else :
                        text = Label(self.WinDlg, text= str(self.score) + "/75", font=("Helvetica", 60))
                        text.place(x = self.Win_w/3+100 ,y = self.Win_h/4+100)

                if self.TestMode == False :
                        if (self.score >= 60):
                                text = Label(self.WinDlg, text= "PASS", font=("Helvetica", 60),foreground="green")
                                text.place(x = self.Win_w/3+100 ,y = self.Win_h/4+200)
                        else:
                                text = Label(self.WinDlg, text= "FAIL", font=("Helvetica", 60),foreground="red")
                                text.place(x = self.Win_w/3+120 ,y = self.Win_h/4+200)
                else :
                        if (self.score*100/75 >= 60):
                                text = Label(self.WinDlg, text= "PASS", font=("Helvetica", 60),foreground="green")
                                text.place(x = self.Win_w/3+100 ,y = self.Win_h/4+200)
                        else:
                                text = Label(self.WinDlg, text= "FAIL", font=("Helvetica", 60),foreground="red")
                                text.place(x = self.Win_w/3+120 ,y = self.Win_h/4+200)
                        

                
                

#===========================================================================================================
        def ChoiceButtonReal(self):

                b_Special = False
                image_size = [0,0]*5

                self.blJudge = True
                
                self.DirSubject =  0
                
                if self.RealModeDir == self.SubjectList[0]:
                        self.DirSubject =  0
                elif self.RealModeDir == self.SubjectList[1]:
                        self.DirSubject =  1
                elif self.RealModeDir == self.SubjectList[2]:
                        self.DirSubject =  2
                elif self.RealModeDir == self.SubjectList[3]:
                        self.DirSubject =  3
                        
                

                self.ChoiceNum = len(os.listdir(self.gamepath_org +'\\'+ self.RealModeDir+ '\\'
                                                + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]))) - 1

                
                self.Question_Img = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+ '\\'
                                               + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\q.PNG')
                
                
                self.Question = Label(self.WinDlg, image = self.Question_Img)                                 

                self.Img_1 = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+'\\'
                                        + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\1.PNG')
                self.Img_2 = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+'\\'
                                        + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\2.PNG')
                self.Img_3 = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+'\\'
                                        + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\3.PNG')
                self.Img_4 = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+'\\'
                                        + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\4.PNG')

                image_size[0] = self.Question_Img.height(),self.Question_Img.width()
                image_size[1] = self.Img_1.height(),self.Img_1.width()
                image_size[2] = self.Img_2.height(),self.Img_2.width()
                image_size[3] = self.Img_3.height(),self.Img_3.width()
                image_size[4] = self.Img_4.height(),self.Img_4.width()

                
                if (image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+image_size[4][0]+200 >= self.Win_h ):

                        b_Special = True

                        

                if self.ChoiceNum == 5 :
                        self.Img_5 = PhotoImage(file= self.gamepath_org +'\\'+ self.RealModeDir+'\\'
                                                + str(self.QuestionRandGet[self.DirSubject][self.QuestionArrNum-1]) + '\\5.PNG')

                self.RadioBtn_1 = Button(self.WinDlg,command = self.ChangeQuestionReal_1    )
                self.RadioBtn_2 = Button(self.WinDlg,command = self.ChangeQuestionReal_2    )
                self.RadioBtn_3 = Button(self.WinDlg,command = self.ChangeQuestionReal_3    )
                self.RadioBtn_4 = Button(self.WinDlg,command = self.ChangeQuestionReal_4    )

                if self.ChoiceNum == 5 :
                        self.RadioBtn_5 = Button(self.WinDlg,command = self.ChangeQuestionReal_5)
                

                self.RadioBtn_1.config(image=self.Img_1)
                self.RadioBtn_2.config(image=self.Img_2)
                self.RadioBtn_3.config(image=self.Img_3)
                self.RadioBtn_4.config(image=self.Img_4)

                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.config(image=self.Img_5)

                if b_Special :
                        self.Question.place(x = 20 ,y = 20)
                        self.RadioBtn_1.place(x = 20 ,y = image_size[0][0]+30)
                        self.RadioBtn_2.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+40)
                        if image_size[1][1] >= image_size[2][1] :
                                self.RadioBtn_3.place(x = 50 + image_size[1][1] ,y = image_size[0][0]+30)
                                self.RadioBtn_4.place(x = 50 + image_size[1][1] ,y = image_size[0][0]+image_size[3][0]+40)
                        else:
                                self.RadioBtn_3.place(x = 60 + image_size[2][1] ,y = image_size[0][0]+30)
                                self.RadioBtn_4.place(x = 60 + image_size[2][1] ,y = image_size[0][0]+image_size[3][0]+40)

                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.place(x = 70 + image_size[1][1] + image_size[3][1] ,y = image_size[0][0]+30)

                else:
                        self.Question.place(x = 20 ,y = 20)
                        self.RadioBtn_1.place(x = 20 ,y = image_size[0][0]+30)
                        self.RadioBtn_2.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+40)
                        self.RadioBtn_3.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+50)
                        self.RadioBtn_4.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+60)


                        if self.ChoiceNum == 5 :
                                self.RadioBtn_5.place(x = 20 ,y = image_size[0][0]+image_size[1][0]+image_size[2][0]+image_size[3][0]+image_size[4][0]+70)

                self.SetColor()
#======================================================================================================================================================
        def ChangeQuestionReal_1(self):
                        
                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="CadetBlue1"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                
                self.AnsSave[self.subject][self.QuestionArrNum-1] = 1
#======================================================================================================================================================
        def ChangeQuestionReal_2(self):
                        
                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="CadetBlue1"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                
                self.AnsSave[self.subject][self.QuestionArrNum-1] = 2

#======================================================================================================================================================
        def ChangeQuestionReal_3(self):
                        
                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="CadetBlue1"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                
                self.AnsSave[self.subject][self.QuestionArrNum-1] = 3

#======================================================================================================================================================
        def ChangeQuestionReal_4(self):
                        
                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="CadetBlue1"))
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="white"))
                
                self.AnsSave[self.subject][self.QuestionArrNum-1] = 4

#======================================================================================================================================================
        def ChangeQuestionReal_5(self):
                        
                self.RadioBtn_1.after(0, self.RadioBtn_1.config(bg="white"))
                self.RadioBtn_2.after(0, self.RadioBtn_2.config(bg="white"))
                self.RadioBtn_3.after(0, self.RadioBtn_3.config(bg="white"))
                self.RadioBtn_4.after(0, self.RadioBtn_4.config(bg="white"))
                if self.ChoiceNum == 5 :
                        self.RadioBtn_5.after(0, self.RadioBtn_5.config(bg="CadetBlue1"))
                
                self.AnsSave[self.subject][self.QuestionArrNum-1] = 5

                
#===========================================================================================================
        def RealTestAuxWindowUpdate(self):

                self.subject =  0
                
                if self.RealModeDir == self.SubjectList[0]:
                        self.subject =  0
                elif self.RealModeDir == self.SubjectList[1]:
                        self.subject =  1
                elif self.RealModeDir == self.SubjectList[2]:
                        self.subject =  2
                elif self.RealModeDir == self.SubjectList[3]:
                        self.subject =  3

                a = [0]*self.SubjectLen

                for i in range (0,self.SubjectLen):
                        for j in range (0,self.RealModeNumQuest):
                                if self.AnsSave[i][j] != 0 :
                                        a[i] += 1
     
                if a[0] == self.RealModeNumQuest:
                        self.SetSubject1.after(0, self.SetSubject1.config(bg="steel blue"))
                if a[1] == self.RealModeNumQuest:
                        self.SetSubject2.after(0, self.SetSubject2.config(bg="steel blue"))
                if a[2] == self.RealModeNumQuest:
                        self.SetSubject3.after(0, self.SetSubject3.config(bg="steel blue"))

                if self.TestMode == False :
                       if a[3] == self.RealModeNumQuest:
                                self.SetSubject4.after(0, self.SetSubject4.config(bg="steel blue"))


                self.SubjectStatus.after(0,self.SubjectStatus.config(text = self.SubjectDisp[self.subject] ,font=("Helvetica", 18) ))
                self.QuestionNumStatus.after(0,self.QuestionNumStatus.config(text ="Question Number "+
                                                                             str(self.QuestionArrNum)+" /"+str(self.RealModeNumQuest)  ,font=("Helvetica", 14) ))

                
                if a[0] != self.RealModeNumQuest:
                        self.SetSubject1.after(0, self.SetSubject1.config(bg="white"))
                if a[1] != self.RealModeNumQuest:
                        self.SetSubject2.after(0, self.SetSubject2.config(bg="white"))
                if a[2] != self.RealModeNumQuest:
                        self.SetSubject3.after(0, self.SetSubject3.config(bg="white"))
                
                if (self.TestMode == False):
                        if a[3] != self.RealModeNumQuest:
                                self.SetSubject4.after(0, self.SetSubject4.config(bg="white"))
                        
                if(self.RealModeDir == self.SubjectList[0]):
                        self.SetSubject1.after(0, self.SetSubject1.config(bg="medium aquamarine"))

                elif(self.RealModeDir == self.SubjectList[1]):
                        self.SetSubject2.after(0, self.SetSubject2.config(bg="medium aquamarine"))

                elif(self.RealModeDir == self.SubjectList[2]):
                        self.SetSubject3.after(0, self.SetSubject3.config(bg="medium aquamarine"))

                elif(self.RealModeDir == self.SubjectList[3]):
                        self.SetSubject4.after(0, self.SetSubject4.config(bg="medium aquamarine"))
                        

                for i in range(0,self.RealModeNumQuest):
                        if self.AnsSave[self.subject][i] == 0 :
                                self.QuestionStatus[i].after(0, self.QuestionStatus[i].config(bg="white"))
                        else:
                                self.QuestionStatus[i].after(0, self.QuestionStatus[i].config(bg="steel blue"))

                                
                        if(i == self.QuestionArrNum-1):
                                self.QuestionStatus[i].after(0, self.QuestionStatus[i].config(bg="medium aquamarine"))
                

                self.Question.after(0,self.Question.destroy)
                self.RadioBtn_1.after(0, self.RadioBtn_1.destroy)
                self.RadioBtn_2.after(0, self.RadioBtn_2.destroy)
                self.RadioBtn_3.after(0, self.RadioBtn_3.destroy)
                self.RadioBtn_4.after(0, self.RadioBtn_4.destroy)
                if self.ChoiceNum == 5 :
                         self.RadioBtn_5.after(0, self.RadioBtn_5.destroy)
                                

                self.ChoiceButtonReal()


#===================================================================================================================
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm Code Here mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#===================================================================================================================
        
game = EnQuiz(0)
game.WinDlg.mainloop()



