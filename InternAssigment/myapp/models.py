from django.db import models



#define a class names studentsmarks with some input filed 
class StudentMarks(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200)
    DOb=models.CharField(max_length=15)
    PhysicsMarks=models.IntegerField()
    ChemistryMarks=models.IntegerField()
    CsMarks=models.IntegerField()
    
    
    #method to calculate the sum of all subject 
    def get_total_marks(self):
        total_marks = self.PhysicsMarks + self.ChemistryMarks + self.CsMarks 
        return total_marks
    
    
    
    #method to calculate the percentage of every student and return it 
    def get_percentage(self):
        total_marks = self.get_total_marks()
        percentage = (total_marks / 300) * 100
        FinalPercentage = round(percentage, 2)
        return FinalPercentage
   
    
