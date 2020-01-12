function create() {
    python create.py $1
    cd
    cd Documents/Projects/$1
    if [ $2 == "web-node" ]
    then
        git init
        npm init -y
        npm install bcryptjs body-parser compression concurrently cookie-parser cors dotenv express jsonwebtoken validator
        npm install --save-dev chai faker mocha nodemon should sinon supertest typescript
        mkdir backend
        cd backend/
        mkdir config models seeders migrations validations middlewares routes services public
        cd ..
        touch server.js .gitignore .env README.md
        echo **/node_modules >> .gitignore
        echo **/.env >> .gitignore
        echo ./node_modules >> .gitignore
        echo .env >> .gitignore
        echo /node_modules >> .gitignore
        echo node_modules >> .gitignore
        if [ $3 == "react" ]
        then
            npx create-react-app frontend
            cd frontend/
            npm install axios classnames http-proxy-middleware jwt-decode react-helmet-async redux react-redux redux-chain redux-thunk
            rm README.md
            cd src/
            mkdir store components containers
            cd store/
            mkdir actions reducers
            touch store.js
            cd ..
            cd ..
            cd ..
        elif [ $3 == 'angular' ]
        then
            ng new frontend
            cd frontend/
            ng add @ngrx/store @ngrx/effects
            npm install jwt-decode rxjs @angular/cli @angular/compiler-cli @angular-devkit/build-angular
            rm README.md
            cd ..
        fi
    fi
    git remote add origin https://github.com/halcika7/$1.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}

function remove() {
    python remove.py $1
}