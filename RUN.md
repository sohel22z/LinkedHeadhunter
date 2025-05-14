pkill -f chromedriver
pkill -f "Google Chrome"

RUN - python3 headhunter.py <linkedin_email> <linkedin_password> <delay_seconds> <page_depth>
<!-- Example -->
<!-- python3 headhunter.py john.doe@gmail.com myPassword123 5 10 -->