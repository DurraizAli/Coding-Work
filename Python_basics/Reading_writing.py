# f=open("D:\\University Data\\Semester 7\\Coding Work\\Python_basics\\funny.txt","r")
# f_out=open("D:\\University Data\\Semester 7\\Coding Work\\Python_basics\\funny_out.txt","r")
# f.write("Java is good langauge but python is good \n it is going to next line")
# f.close()

# for line in f:
#     tokens=line.split(' ')
#     f_out.write("wordcount:"+str(len(tokens))+" "+line)
# f.close()
# f_out.close()
#---------------------------------------------------------
# def countnum(num):
#     df=0
#     exrcs=open("D:\\University Data\\Semester 7\\Coding Work\\Python_basics\\Exercise.txt","r")
#     for line in exrcs:
#         tokens=line.split()
#         # print(str(tokens))
#         if(num in str(tokens)):
#             df+=1
#     print(df)
#     exrcs.close()
# countnum("100")
#-------------------------------------------------------
input_file=open("D:\\University Data\\Semester 7\\Coding Work\\Python_basics\\Exercise.txt","r+")
output_file= open("D:\\University Data\\Semester 7\\Coding Work\\Python_basics\\funny_out.txt","r+")

for line in input_file:
    numbers= line.strip().split(",")
    num1= int(str(numbers[0]))
    num2= int(str(numbers[1]))
    total= num1+num2
    updated_line= f"{line.strip()},{total}\n"
    output_file.write(updated_line)
    

    
input_file.close()
output_file.close()