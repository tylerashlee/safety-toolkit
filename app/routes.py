from flask import Blueprint, render_template, request
from app.utils import evaluate_password

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/quiz')
def quiz():
    questions = [
        {
            'id': 1,
            'question': 'What is phishing?',
            'options': [
                'A technique used to guess someone’s password by brute force',
                'A fraudulent attempt to obtain sensitive information via email or messages',
                'A method of hacking into databases using malware'
            ]
        },
        {
            'id': 2,
            'question': 'What is doxxing?',
            'options': [
                'Sending unwanted files to someone\'s computer',
                'Publicly sharing someone’s private or personal information without consent',
                'Hacking into someone’s device using spyware'
            ]
        },
        {
            'id': 3,
            'question': 'What is a "deepfake"?',
            'options': [
                'A fake antivirus alert designed to trick users',
                'A tool used to scan fake websites',
                'A digitally manipulated video or audio clip that appears real'
            ]
        },
        {
            'id': 4,
            'question': 'What is multi-factor authentication?',
            'options': [
                'Logging in with your username and a password',
                'A security feature requiring two or more types of verification',
                'Using the same password on multiple sites for convenience'
            ]
        },
        {
            'id': 5,
            'question': 'Why should you use a unique password for each account?',
            'options': [
                'It’s easier to remember a variety of passwords',
                'To reduce the risk of multiple accounts being compromised if one is exposed',
                'To meet most websites’ password requirements'
            ]
        },
        {
            'id': 6,
            'question': 'How often should you change your password for your accounts?',
            'options': [
                'Once every five years',
                'Only when there is a security breach',
                'Only when prompted by the website'
            ]
        },
        {
            'id': 7,
            'question': 'What should you do if you receive a link from an unknown number or email?',
            'options': [
                'Click it quickly to see where it goes',
                'Forward it to your friends to warn them',
                'Avoid clicking and delete or report the message'
            ]
        },
        {
            'id': 8,
            'question': 'Why should you be careful with oversharing online?',
            'options': [
                'It can make your content less interesting',
                'It might make people unfollow you',
                'It can expose personal details that hackers or stalkers can exploit'
            ]
        },
        {
            'id': 9,
            'question': 'Why should you avoid using public Wi-Fi for sensitive transactions?',
            'options': [
                'It’s usually too slow for banking apps',
                'It can be easily monitored by attackers',
                'It drains your battery faster'
            ]
        },
         {
            'id': 10,
            'question': 'How can AI be used maliciously in cybersecurity attacks?',
            'options': [
                'By helping users detect strong passwords',
                'By generating convincing phishing emails or deepfake messages',
                'By scanning for system updates faster'
            ]
        },
        # ...repeat for all questions
    ]
    return render_template('quiz.html', questions=questions)

@main.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    correct_answers = [
    'A fraudulent attempt to obtain sensitive information via email or messages',  # Q1
    'Publicly sharing someone’s private or personal information without consent',  # Q2
    'A digitally manipulated video or audio clip that appears real',  # Q3
    'A security feature requiring two or more types of verification',  # Q4
    'To reduce the risk of multiple accounts being compromised if one is exposed',  # Q5
    'Only when there is a security breach',  # Q6
    'Avoid clicking and delete or report the message',  # Q7
    'It can expose personal details that hackers or stalkers can exploit',  # Q8
    'It can be easily monitored by attackers',  # Q9
    'By generating convincing phishing emails or deepfake messages'  # Q10
    ]

    score = 0
    for i, correct in enumerate(correct_answers):
        user_answer = request.form.get(f'q{i + 1}')  # q1, q2, q3, etc.
        if user_answer == correct:
            score += 1
    return render_template('quiz_result.html', score=score, total=len(correct_answers))

@main.route('/checklist')
def checklist():
    return render_template('checklist.html')

@main.route('/password', methods=['GET', 'POST'])
def password():
    strength = None
    feedback = ''
    if request.method == 'POST':
        password = request.form.get('password')
        strength, feedback = evaluate_password(password)
    return render_template('password.html', strength=strength, feedback=feedback)

@main.route('/mission')
def mission():
    return render_template('mission.html')

@main.route('/privacy-check')
def privacy_check():
    return render_template('privacy_check.html')

@main.route('/privacy-results', methods=['POST'])
def privacy_results():
    responses = request.form
    advice = []

    # Logic based on responses
    if responses.get('visibility') == 'Public':
        advice.append("Consider setting your account to private for better privacy.")

    if 'address' in responses or 'workplace' in responses or 'school' in responses:
        advice.append("Avoid sharing sensitive personal info like your address or workplace.")

    if responses.get('location_sharing') in ['Frequently', 'Sometimes']:
        advice.append("Limit real-time location sharing to avoid being tracked.")

    if responses.get('tagging') == 'Yes':
        advice.append("Adjust your tagging settings to approve tags before they appear.")

    if responses.get('old_posts') == 'No':
        advice.append("Review old posts and remove anything sensitive or revealing.")

    if responses.get('twofa') != 'Yes':
        advice.append("Enable two-factor authentication (2FA) to protect your account.")

    return render_template('privacy_results.html', advice=advice)