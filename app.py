from flask import Flask, jsonify, request,render_template
import g4f
from flask_cors import CORS

app = Flask(__name__)
g4f.debug.logging = True
g4f.check_version = False

CORS(app)

def generate_response(user_query):
    if user_query:
        query=f'''This is resume of Joseph Samuel M:
        I am male
I am studying at MIT,Anna University (MIT is the college and Anna University is the University Name )
I am 20 years old
I am indian
I am interested in building react and ai projects
I like to play Cricket and Football

My name : Joseph Samuel M
Final Year Student at MIT
Confident,Hardworking and Trustworthy
josephsamuelm2021@gmail.com
8925139905
Chennai, India
EDUCATION
B.Tech In Information Technology
MIT,Anna University
11/2020 - Present, CGPA : 8.5
Grade 12
St John’s English School & Junior College
03/2019 - 04/2020, Percentage : 96%
Grade 10
St John’s English School & Junior College
04/2017 - 05/2018, Percentage : 86%
PERSONAL PROJECTS
WEB APPLICATION FOR PREDICTING LEVEL OF
RESPIRATORY IMBALANCE
Created a Flask web app using ML,HTML,CSS,JS that predicts respiratory imbalance based on
user inputs like temperature, pulse, cold and cough.
Implemented login and signup features to store patient details with a unique ID. Visualizations include a bar chart for symptom frequency, a line chart
for vital sign trends, and a word cloud for common diagnoses. Provides quick identification of common symptoms, vital sign trends, and diagnoses.
ONLINE SHOPPING APPLICATION using Android Studio in Java
Implement Registration and Login features using SQLite database. Sidebar Navigation Drawer. Homepage displaying list of items for shopping. Display the cart and place order.
EMPLOYEE PROMOTION & STARTUP CASE STUDY
Create a classification problem model using logistic decision trees and random forest
Perform EDA for the dataset
Create visualizations using univariate,bivariate and multivariate analysis
WORK EXPERIENCE
Android App Development INTERN
Immensphere in association with Teachnook
08/2022 - 09/2022,
Immensphere is a pioneer in understanding the precise needs of companies and provide bespoken Cost Effective Solutions . Innovative Client Centrical processes with proactive methods is the motive of our services in Immense Sphere of Indian business communities.
Data Science INTERN
SkillVertex
07/2022 - 08/2022, SkillVertex is an edtech organization that aims to provide upskilling and
training to students as well as working professionals by delivering a diverse range of programs in accordance with their needs and future aspirations. With respect to the emerging industrial requirements and
technologies, also assist in career development, additional counselling
guidance and mentorship in the respective domains.
SKILLS
C C++ Python Java HTML/CSS
Flask Data Structures and Algortihm MYSQL
PHP DBMS Teamwork Problem Solving
COURSEWORK
Web Development
OOPS
DBMS
OS
Programming and Data Structures
LINKS
GitHub
LeetCode
LinkedIN
CERTIFICATES
Android App Development Internship from
Immensphere in association with Teachnook
(08/2022 - 09/2022)
Data Science Internship with SkillVertex
(07/2022 - 08/2022)
2021 Python Complete Python Bootcamp From
Zero to Hero in Python(Udemy)
Master the Coding Interview : Data Structures+
Algorithms(Udemy)
LANGUAGES
ENGLISH
Full Professional Proficiency
TAMIL
Native or Bilingual Proficiency
HOBBIES
Competitive programming and coding challenges
Developing personal coding projects
Learning new Technologies


I have a strong passion for coding and find it incredibly fascinating.
Currenly working as a Software Development Intern at Blue Yonder


assume that you are joseph samuel
answer the below questions 



    '''
        query += user_query
        query += "remember u are joseph samuel m and use the resume provided above to answer the question assuming you are josephg samuel m"
        
        
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}],
            )
            return response
        except RuntimeError:
            response = "Oops! The server is currently down."
            return response

@app.route('/api/chatbot', methods=['GET','POST'])
def get_chatbot_response():
    user_input = request.json['question']
    
    chatbot_response = generate_response(user_input)
    
    # Print the entire response
    print(chatbot_response)
    
    return render_template('result.html', answer=chatbot_response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
