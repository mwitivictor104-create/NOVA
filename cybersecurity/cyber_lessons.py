LESSONS = {
    1: {
        "title": "Introduction to Cybersecurity",
        "content": """
Cybersecurity is the practice of protecting computers,
networks, applications and information from unauthorized
access, damage or misuse.

Blue Team:
- Monitoring
- Detection
- Incident response
- System defense

Red Team:
- Authorized security testing
- Vulnerability discovery
- Security assessment

Important rule:
Only test systems that you own or have explicit permission
to test.
"""
    },

    2: {
        "title": "Networking Fundamentals",
        "content": """
Before learning security tools, understand networking.

Important concepts:
- IP addresses
- MAC addresses
- Ports
- TCP and UDP
- DNS
- HTTP and HTTPS
- Routers
- Firewalls
"""
    },

    3: {
        "title": "Nmap Introduction",
        "content": """
Nmap is a network discovery and security-auditing tool.

It can help identify:
- Hosts
- Open ports
- Network services
- Service versions

Only scan networks and devices that you own or are
authorized to test.
"""
    },

    4: {
        "title": "Wireshark Introduction",
        "content": """
Wireshark is a network protocol analyzer.

It allows security professionals to examine network
packets and understand how devices communicate.

Important concepts:
- Packets
- Protocols
- Source and destination
- TCP
- UDP
- DNS
- HTTP
"""
    },

    5: {
        "title": "Burp Suite Introduction",
        "content": """
Burp Suite is a web-security testing platform.

It helps security testers understand HTTP requests
and responses and identify vulnerabilities.

Practice only with your own applications or authorized
training laboratories.
"""
    },

    6: {
        "title": "Kali Linux",
        "content": """
Kali Linux is a Linux distribution designed for security
testing and digital forensics.

It contains many cybersecurity tools.

Learning Linux commands first will make Kali easier to
understand.
"""
    },

    7: {
        "title": "Log Analysis",
        "content": """
Security teams use logs to investigate activity.

Examples include:
- Login attempts
- Server events
- Application errors
- Network events
- Security alerts

Tools such as Splunk and ELK can help analyze large
amounts of log data.
"""
    }
}


def get_lesson(number):
    lesson = LESSONS.get(number)

    if not lesson:
        return "Lesson not found."

    return (
        f"CYBERSECURITY LESSON {number}: "
        f"{lesson['title']}\n\n"
        f"{lesson['content']}"
    )


def list_lessons():
    result = "NOVA CYBERSECURITY LESSONS\n\n"

    for number, lesson in LESSONS.items():
        result += f"{number}. {lesson['title']}\n"

    return result
