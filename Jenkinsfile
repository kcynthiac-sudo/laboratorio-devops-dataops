pipeline {
    agent any

    stages {

        stage('Validar Python') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" --version'
            }
        }

        stage('Instalar dependencias') {
    steps {
        bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" -m pip install pandas'
        bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" -m pip install psycopg2-binary'
    }
}

        stage('Ejecutar procesamiento') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" scripts\\procesamiento.py'
            }
        }

        stage('Validación final') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}
