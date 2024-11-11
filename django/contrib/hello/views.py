import random
from django.http import HttpResponse

def hello_world(request):
    greetings = [
        ("👋 Hello, World!", "#667eea, #764ba2"),
        ("🌟 Welcome, Explorer!", "#4facfe, #00f2fe"),
        ("🚀 Hi there, Astronaut!", "#fa709a, #fee140"),
        ("🌈 Greetings, Friend!", "#43e97b, #38f9d7"),
        ("✨ Hey, Wonderful!", "#f6d365, #fda085")
    ]
    greeting, gradient = random.choice(greetings)
    color1, color2 = gradient.split(',')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Greeting</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: linear-gradient(135deg, {color1} 0%, {color2} 100%);
            }}
            .greeting {{
                background: white;
                padding: 2rem 4rem;
                border-radius: 1rem;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h1 {{
                color: #2d3748;
                font-size: 2.5rem;
                margin: 0;
                animation: wave 2s infinite;
            }}
            @keyframes wave {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-10px); }}
            }}
        </style>
    </head>
    <body>
        <div class="greeting">
            <h1>{greeting}</h1>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
