def get_skills():
    return ["Python","C++", "Javascript", "Juggling", "Running", "Eating"]

def show_skills(skills):
    print()
    for count,skill in enumerate(skills,1):
     print (f"{count}. {skill}")

def get_user_skills(skills):
   show_skills(skills)
   chosen_skills= [input("\nChoose a skill from above by entering its number:"),input("Choose a skill from above by entering its number:")]
   return [skills[int(skill)-1] for skill in chosen_skills]

def get_user_cv(skills):
    return{
         "name" : input("What's your name? "),
         "age" : int(input("How old are you? ")),
         "experience" : int(input("How many years of experience do you have? ")),
         "skills" : get_user_skills(skills)
}
  
def check_acceptance(cv, desired_skill):
    return (cv["age"] >= 25 
    and cv["age"] <= 40 and cv["experience"] > 3 
    and desired_skill in cv["skills"])
    
def main():
   print("Welcome to the special recruitment program, please answer the following questions:")
   
   skills = get_skills()
   desired_skill = 2

   cv = get_user_cv(skills)
  
   if(check_acceptance(cv, skills[desired_skill])):
       print(f"Congratulation...you have been accepted, {cv['name']}.")
   else:
       print(f"Sorry...you have been rejected, {cv['name']}.")


if __name__ == "__main__":
    main()
