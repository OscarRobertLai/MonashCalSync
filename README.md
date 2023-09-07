# MonashCalSync

Setup Git



https://www.robinwieruch.de/mac-setup-web-development/

>git clone git@github.com:OscarRobertLai/MonashCalSync.git
> 
> 
> pip install virtualenvwrapper
>

Install virtualenvwrapper:

macOS/Linux: 1
> pip install virtualenvwrapper

Add the following to shell config (.bashrc, .zshrc):
bash
Copy code

>export WORKON_HOME=$HOME/.virtualenvs
> source /usr/local/bin/virtualenvwrapper.sh
> 
Source your shell config: 
>source ~/.zshrc
Create an environment: 
> mkvirtualenv calsync

Activate it: workon myenv

Deactivate: deactivate

List envs: lsvirtualenv

## here is a lint for testit
