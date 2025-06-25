### by without using sum()

class student:
    def __init__(self,n,r,sub={}):
        self.name=n
        self.roll=r
        self.subjects=sub
        
    def cal_percentage(self):
        if len(self.subjects) == 5:
            total = 0
            for marks in self.subjects.values():
                total += marks
            subs = len(self.subjects)
            percentage = total / (subs * 100) * 100
            return percentage

    def display_info(self):
        print(f"name of student: {self.name}")   
        print(f"roll no of student: {self.roll}")
        print(f"marks for students in subject")
        for subject,marks in self.subjects.items():
            
             print(f"{subject} : {marks}")
        print(f"persentage of student = {self.cal_percentage():.2f}%")

s1=student("neha",1,{"Eng":56,"Maths":85,"Science":78,"Hindi":65,"marathi":88})
s1.display_info()     
s2=student("pooja",2,{"Eng":54,"Maths":56,"Science":87,"Hindi":66,"marathi":46})           
s2.display_info()       


