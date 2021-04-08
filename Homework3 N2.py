class Testpaper():
    def __init__(self,subject,mark_scheme,pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark

    def get_subject(self):
        return self.subject

    def get_mark_scheme(self):
        return self.mark_scheme

    def get_pass_mark_and_convert_to_float(self):
        return  self.pass_mark.strip('%')



paper1 = Testpaper("Maths",["1A","2C","3D","4A","5A"],"60%")
paper2 = Testpaper("Chemistry",["1C","2C","3D","4A"],"75%")
paper3 = Testpaper("Computing",["1D","2C","3C","4B","5D","6C","7A"],"75%")



class Student(Testpaper):

    def __init__(self,tests_taken = 'No Tests Taken'):

        self.tests_taken = tests_taken

    def take_tests(self,test_object,stud_grades):

        self.tests_taken ={f"{test_object}":f"{stud_grades}"}

        key = Testpaper.get_subject(test_object)                                        #Testpaper ატრიბუტების წამოღება
        answers = Testpaper.get_mark_scheme(test_object)
        passing_score = int(Testpaper.get_pass_mark_and_convert_to_float(test_object))
        value = stud_grades
        checklist = [item for item in answers if item not in value]
        stud_score = int((len(answers)-len(checklist))/len(answers)*100)
        for i,x in self.tests_taken.items():
            if stud_score>=passing_score:
                print(key,":",f"Passed! ({round(stud_score)}%)")
            else:
                print(key, ":", f"Failed! ({round(stud_score)}%)")






student1 = Student()
student2 = Student()
student3 = Student()
print(student3.tests_taken)
student1.take_tests(paper1,["1C","2D","3D","4A","5A"])
student2.take_tests(paper2,["1C","2D","3A","4C"])
student2.take_tests(paper3,["1A","2C","3A","4C","5D","6C","7B"])



















