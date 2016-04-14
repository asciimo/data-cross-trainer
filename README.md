Setting up flask
===
    mkdir data_crosstrainer
    cd data_crosstrainer
    git init
    echo venv >> .gitignore
    virtualenv venv
    source venv/bin/activate
    pip install Flask
    pip install requests
    

Setting up EC2
===
    sudo yum install git
    git clone https://github.com/asciimo/data-cross-trainer.git
    sudo pip install Flask
    sudo python data_crosstrainer.py 
    

