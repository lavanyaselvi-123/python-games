print("Hi Welcome to Quiz World")
print("Let's play...")
start=True

while start:
    ans=input("\nyes/no\n")
    if ans.lower()=='yes':
        score=0
        q=5
        ans=input('Choose the domain\n a)India\n b)Solar System\n c)Science\n d)General Knowledge\n')
        if ans.lower()=='a':
            ans=input("1.What is the capital of India?\n a)Chennai\n b)Mumbai\n c)Kolkatta\n d)New Delhi\n")
            if ans.lower()=='d':
                score+=1
            ans=input("How many states are there in India?\n a)32\n b)29\n c)30\n d)31\n")
            if ans.lower()=='b':
                score+=1
            ans=input("Which is the largest state in India(by area)?\n a)Tamilnadu\n b)Kerala\n c)Rajasthan\n d)Maharastra\n")
            if ans.lower()=='c':
                score+=1
            ans=input("Which state has largest population in India?\n a)Uttarpradesh\n b)Tamilnadu\n c)Kerala\n d)Rajasthan\n")
            if ans.lower()=='a':
                score+=1
            ans=input("Who is the prime minister of India?\n a)Narendra Modi\n b)Rajiv Gandhi\n c)Vajpai\n d)Jayalalitha\n")
            if ans.lower()=='a':
                score+=1
            print("You've got",score,"questions correct")
            mark=(score/q)*100;
            print(str(mark),"%")    
        elif ans.lower()=='b':
            ans=input("1.Which is the largest planet?\n a)Mercury\n b)Earth\n c)Mars\n d)Jupiter\n")
            if ans.lower()=='d':
                score+=1
            ans=input("How many planets are there in solar system?\n a)9\n b)8\n c)7\n d)6\n")
            if ans.lower()=='b':
                score+=1
            ans=input("Which planet is called as Blue planet?\n a)Venus\n b)Earth\n c)Neptune\n d)Uranus\n")
            if ans.lower()=='c':
                score+=1
            ans=input("In which planet living organisms can live?\n a)Earth\n b)Mars\n c)Mercury\n d)Saturn\n")
            if ans.lower()=='a':
                score+=1
            ans=input("Who discovered Solar system?\n a)Copernicus\n b)Vasco Da Gama\n c)Newton\n d)Murphy\n")
            if ans.lower()=='a':
                score+=1
            print("You've got",score,"questions correct")
            mark=(score/q)*100;
            print(str(mark),"%")      
        elif ans.lower()=='c':
            ans=input("1.Who is the father of physics?\n a)Rajan\n b)Keerthan\n c)Lavan\n d)Newton\n e)Sobian\n")
            if ans.lower()=='d':
                score+=1
            ans=input("What is the colour of Blood of human?\n a)yellow\n b)Red\n c)Blue\n d)Green\n")
            if ans.lower()=='b':
                score+=1
            ans=input("How many bones are there in human body?\n a)203\n b)205\n c)206\n d)204\n")
            if ans.lower()=='c':
                score+=1
            ans=input("Which of the following is not a green house gas?\n a)HCL\n b)CO2\n c)HFC\n d)HCFC\n")
            if ans.lower()=='a':
                score+=1
            ans=input("Who is the father of biology?\n a)Aristotle\n b)Rajstotle\n c)Lavstotle\n d)Keerstotle\n e)Sobstotle\n")
            if ans.lower()=='a':
                score+=1
            print("You've got",score,"questions correct")
            mark=(score/q)*100;
            print(str(mark),"%")      
        elif ans.lower()=='d':
            ans=input("1.How many colours are there in Rainbow?\n a)9\n b)8\n c)10\n d)7\n")
            if ans.lower()=='d':
                score+=1
            ans=input("What is baby frog known?\n a)Lavpole\n b)Tadpole\n c)Rajpole\n d)Keerpole\n e)Sobpole\n")
            if ans.lower()=='b':
                score+=1
            ans=input("How many days in a year?\n a)367\n b)366\n c)365\n d)364\n")
            if ans.lower()=='c':
                score+=1
            ans=input("2+2*2-2/2?\n a)5\n b)4\n c)6\n d)7\n")
            if ans.lower()=='a':
                score+=1
            ans=input("Which is the largest continent?\n a)None of these\n b)Europe\n c)America\n d)Australia\n")
            if ans.lower()=='a':
                score+=1
            print("You've got",score,"questions correct")
            mark=(score/q)*100;
            print(str(mark),"%")  
    else:
        print("Thank you for participating")
        start=False
    

