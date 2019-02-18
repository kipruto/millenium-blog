import datetime
users = []
comments = []


class User():
    def __init__(self, email=None, password=None, role=None, loggedInAt= None):
        self.email = email
        self.password = password
        self.role = role
        self.loggedInAt = loggedInAt
    
    def signup(self):
        self.username = input("\n\n\n REGISTRATION \n Enter your username : \n")
        self.password = input("Please enter your password : \n")
        self.role =input("Choose your role : \n")
        user = {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
        users.append(user)
        print("Registration successfull!")
        print(users)
    
    def login(self):

        self.username = input("LOG IN \n Email : \n")
        self.password = input("Password : \n")
        for user in users:
            if user["email"] == self.username and user["password"] == self.password:
                timestamp = datetime.datetime.now()
                user["loggedInAt"] = timestamp
                print("Successfully logged in at ")
                print(timestamp)
                if user["role"] == "Admin":
                    comment1 = Comment()
                    comment1.addComment()
                    comment1.editComment()
                    comment1.delete()
                    self.logout()
                elif user["role"] == "Moderator":
                    comment1 = Comment()
                    comment1.addComment()
                    comment1.editComment()
                    comment1.delete()
                    self.logout()
                elif user["role"] == "Normal":
                    comment1 = Comment()
                    comment1.addComment()
                    comment1.editComment()
                else:
                    print("invalid role")
                return True
            
            else:
                print("Invalid email/password") 
                return False
    def logout(self):
        users = []
        print("successfully logged out \n\n\n\n")


class Comment():
    def addComment(self):
        user1 = User()
        message = input("ADD COMMENT SECTION \n Kindly add the comment message \n")
        for user in users:
            if user1.username == user["username"]:
                author = user1.username
        timestamp = datetime.datetime.now()
        id = len(comments) + 1
        new_comment = {
            "id":id,
            "message":message,
            "timestamp":timestamp
        }
        comments.append(new_comment)
        print("\n Comment added successfully \n ")
        print("\n comment: " + str(new_comment["message"]) + "\n")
        print("\n Added at \n")
        print(timestamp)
    
    def editComment(self):
        id = input("\n Enter the comment id to edit \ns")
        message = input("\n EDITTING SECTION \n Kindly enter the new comment message \n")
        timestamp = datetime.datetime.now()
        for comment in comments:
            if comment["id"] == int(id):
                index = int(id) - 1
                comments[index]["message"] = message
                print("\n Successfully updated \n")
                print(timestamp)
                print(comment)

        

    def delete(self):
        id = input("Enter the comment id to delete \ns")
        timestamp = datetime.datetime.now()
        for comment in comments:
            if comment["id"] == int(id):
                comments.remove(comment)
                print(timestamp)
                print(comments)


user = User()
user.signup()
user.login()