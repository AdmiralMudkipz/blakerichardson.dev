from django.shortcuts import render
from django.http import Http404
from .models import Computed
from django.utils import timezone


PROJECTS = {
    'nature-picture': {
        'slug': 'nature-picture',
        'title': 'Nature Picture',
        'subtitle': 'Product Manager • Full Stack Web App',
        'description': 'E-commerce site for local artists. Features user signup, profiles, artwork listings, ordering, and notifications. Python/Django backend with TypeScript & React frontend, MySQL database. Managed via Agile/Scrum with Trello.',
        'long_description': (
            'Nature Picture is a full-stack e-commerce platform designed to connect local artists with buyers. '
            'The application features a complete user authentication system with signup and profile management, '
            'artwork browsing and listing capabilities, a full ordering pipeline with notifications, and an admin dashboard. '
            'The backend is built with Python and Django, while the frontend uses TypeScript and React for a responsive, '
            'modern user experience. All data is stored in a MySQL relational database. '
            'The team followed Agile/Scrum methodology using Trello to manage sprints, tasks, and deliverables.'
        ),
        'github': 'https://github.com/AdmiralMudkipz/Nature-Picture',
        'skills': ['Python', 'JavaScript', 'Bash', 'HTML', 'CSS', 'SQL', 'React', 'MySQL', 'Git', 'Networking', 'Hosting', 'Agile/Scrum', 'OOP'],
    },
    'senior-project': {
        'slug': 'senior-project',
        'title': 'Senior Project',
        'subtitle': 'Full Stack Web Application (WIP)',
        'description': 'Enables doctors to administer the Philadelphia Pointing Span Test, measuring reaction to stimuli. Built with Python/Django, HTMX, JavaScript, and MySQL. Iterative Agile Scrum development with the sponsor.',
        'long_description': (
            'This senior capstone project is a web application that allows medical professionals to administer '
            'the Philadelphia Pointing Span Test — a cognitive assessment that measures a patient\'s reaction to visual stimuli. '
            'The system records test sessions, tracks patient data, and presents results in an intuitive interface. '
            'Built with Python/Django on the backend, HTMX for dynamic UI updates without heavy JavaScript frameworks, '
            'and MySQL for data persistence. Development follows iterative Agile Scrum methodology in close '
            'communication with the project sponsor to meet their clinical specifications.'
        ),
        'github': 'https://github.com/MatthewMaselli87/Senior-Project-Spring-2026',
        'skills': ['Python', 'JavaScript', 'Bash', 'HTML', 'CSS', 'SQLite', 'Django', 'HTMX', 'Git', 'Networking', 'Hosting', 'Agile/Scrum', 'OOP'],
    },
    'embedded-systems': {
        'slug': 'embedded-systems',
        'title': 'Embedded Systems',
        'subtitle': 'Arduino • C++',
        'description': 'Classwork and final project: a solar-powered transit arrival sign using NJTransit\'s API, Arduino microcontrollers, and an LED array. Involved sensors, displays, outputs, and circuit design.',
        'long_description': (
            'This embedded systems project involves designing and building a solar-powered transit arrival sign. '
            'The system queries NJTransit\'s API to fetch real-time arrival data, processes it on an Arduino microcontroller, '
            'and displays upcoming arrivals on an LED array. The coursework covered working with sensors, LCD/LED displays, '
            'serial communication, and circuit design. The final project brings all of these concepts together into a '
            'practical, self-sustaining device that could be deployed at a bus stop.'
        ),
        'github': None,
        'skills': ['C++', 'Bash', 'Circuit Design', 'Networking'],
    },
    'operating-systems': {
        'slug': 'operating-systems',
        'title': 'Operating Systems',
        'subtitle': 'C++ • XINU Linux',
        'description': 'Built a terminal for a fork of XINU Linux. Low-level operating system programming in C++.',
        'long_description': (
            'In this operating systems course project, I built a functional terminal shell for a fork of the XINU '
            'educational operating system. The work involved low-level C++ programming including process management, '
            'memory allocation, inter-process communication, and system calls. This project deepened my understanding '
            'of how operating systems manage hardware resources, schedule processes, and provide abstractions to user-space programs.'
        ),
        'github': None,
        'skills': ['C++', 'Bash', 'Operating Systems', 'Data Structures'],
    },
    'led-segment-clock': {
        'slug': 'led-segment-clock',
        'title': 'LED Segment Clock',
        'subtitle': 'C • Computer Lab Techniques',
        'description': 'Created a digital LED 7-segment display clock in C with buttons and addressable segments.',
        'long_description': (
            'This computer lab techniques project involved designing and programming a digital clock using 7-segment '
            'LED displays. Written entirely in C, the clock features button-based time setting, addressable display segments, '
            'and accurate timekeeping logic. The project required understanding of hardware-level I/O, bit manipulation, '
            'and real-time display refresh techniques.'
        ),
        'github': None,
        'skills': ['C', 'Bash'],
    },
    'ftc-robotics': {
        'slug': 'ftc-robotics',
        'title': 'FTC Robotics',
        'subtitle': 'Java • Machine Learning • Team 15458',
        'description': 'Autonomous and driver-controlled programming for competition robot. Used ML visual processing and QR code scanning. Collaborated with the team on deliverables and community outreach.',
        'long_description': (
            'As Lead Programmer for FTC Robotics Team 15458 (Green Machine), I developed both the autonomous and '
            'driver-controlled programs for our competition robot in Java. The autonomous mode used machine learning-based '
            'visual processing to detect the robot\'s environment and react accordingly, including scanning QR codes for '
            'information. The role also involved extensive troubleshooting, debugging, wiring, CAD and 3D printing, '
            'collaborative teamwork, presentations, mentoring younger teammates in Java, and community outreach and fundraising.'
        ),
        'github': 'https://github.com/AdmiralMudkipz/15458-Robotics-Programming-22-23',
        'skills': ['Java', 'Git', 'Circuit Design', 'OOP'],
    },
    'portfolio-website': {
        'slug': 'portfolio-website',
        'title': 'This Portfolio Website',
        'subtitle': 'Full Stack Web Application',
        'description': 'This portfolio site, built with Python/Django, HTMX, and Tailwind CSS. Features project showcases, skill filtering, and responsive design.',
        'long_description': (
            'This portfolio website is the site you are currently viewing. Built from scratch with Python and Django '
            'on the backend, HTMX for seamless dynamic interactions, and Tailwind CSS for styling. '
            'It features project showcases with detail pages, skill-based filtering, responsive design for all devices. '
            'The source code is publicly available on GitHub.'
        ),
        'github': 'https://github.com/AdmiralMudkipz/blakerichardson.dev',
        'skills': ['Python', 'JavaScript', 'Bash', 'HTML', 'CSS', 'Django', 'HTMX', 'Git', 'Networking', 'Hosting'],
    },
}

ALL_SKILLS = sorted({skill for p in PROJECTS.values() for skill in p['skills']})





def is_prime(request, value):
    try:
        num = int(value)
        divisor = None
        
        if num <= 1:
            is_prime_bool = False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    divisor = i
                    break
            
            is_prime_bool = divisor is None
        
        return render(
            request,
            "Portfolio/is_prime.html",
            {
                'input': num,
                'is_prime': is_prime_bool,
                'divisor': divisor
            }
        )
    except (ValueError, TypeError):
        raise Http404(f"Invalid input: {value}")


def compute(request, value):
    try:
        input = int(value)
        precomputed = Computed.objects.filter(input=input)
        if precomputed.count() == 0:
            answer = input * input
            time_computed = timezone.now()
            computed = Computed(
                input=input, 
                output=answer,
                time_computed=time_computed
            )
            computed.save()
        else: 
            computed = precomputed.first()
        
        return render (
            request,
            "Portfolio/compute.html",
            {
                'input': input,
                'output': computed.output,
                'time_computed': computed.time_computed.strftime("%m-%d-%Y %H:%M:%S UTC")
            }
        )
    except:
        raise Http404(f"Invalid input: {value}")

def homepage(request):
    return render(request, "portfolio/homepage.html", {
        'projects': PROJECTS.values(),
        'all_skills': ALL_SKILLS,
    })


def project_detail(request, slug):
    project = PROJECTS.get(slug)
    if not project:
        raise Http404(f"Project not found: {slug}")
    return render(request, "portfolio/project_detail.html", {
        'project': project,
    })


def projects_by_skill(request, skill):
    matching = [p for p in PROJECTS.values() if skill in p['skills']]
    if not matching:
        raise Http404(f"No projects found for skill: {skill}")
    return render(request, "portfolio/projects_by_skill.html", {
        'skill': skill,
        'projects': matching,
        'all_skills': ALL_SKILLS,
    })



    