pipeline {
    agent any
    environment {
        TEST_VAL = "15"
        WEB_UI_TEST_PATH = "/tmp"
    }
    parameters {
        string(name: 'Caption', defaultValue: '=== TESTING ===', description: '')
        booleanParam(name: 'JUNIT', defaultValue: true, description: '')
    }

    stages {
        stage('hillel_git') {
            steps {
                checkout([
                $class: 'GitSCM',
                branches: [[name: '*/main']],
                extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'git_dir']],
                userRemoteConfigs: [[credentialsId: 'git-creds',
                                     url: 'git@github.com:antohaUa/AQA_241007_Hillel.git']]])
            }
        }


        stage('test-execution') {
            steps {
                script {
                    dir('git_dir/Lesson_31_Jenkins/rozetka'){
                        withPythonEnv('python3') {
                            sh """
                                echo "${Caption}"
                                pip install -r requirements.txt
                                # pytest has exit code 1 if tests fail. We return true to be able continue flow.
                                if [ -z "${JUNIT}" ]; then
                                    pytest -sv ./test_check_smartphones.py --alluredir=${WORKSPACE}/allure-results
                                else
                                    pytest -sv ./test_check_smartphones.py --alluredir=${WORKSPACE}/allure-results --junit-xml=test_output.xml
                                fi
                            """
                        }
                    }
                }
            }
            post {
                always {
                        allure includeProperties:
                        false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                }
            }
        }
    }
}