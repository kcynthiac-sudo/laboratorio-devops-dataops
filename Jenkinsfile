pipeline {
    agent any

    stages {

        stage('Validar Python') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.13-64\\python.exe" --version'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.13-64\\python.exe" -m pip install pandas'
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.13-64\\python.exe" -m pip install psycopg2-binary'
            }
        }
        stage('Mostrar script') {
    steps {
        bat 'type scripts\\procesamiento.py'
    }
}

        stage('Ejecutar procesamiento') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\pythoncore-3.13-64\\python.exe" scripts\\procesamiento.py'
            }
        }

        stage('Validación final') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}