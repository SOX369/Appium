pipeline {
    // 指定在任意可用节点运行 (你的是本地 Windows 节点)
    agent any

    options {
        // 保持构建历史最多 10 个，防止磁盘占满
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Checkout Code') {
            steps {
                // 自动拉取 Git 代码 (对应 Freestyle 的 Source Code Management)
                // Jenkins 会根据任务配置自动检出到 Workspace
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                // 打印版本信息，确认环境正常
                bat 'D:\\Anaconda3\\envs\\DL\\python.exe --version'
                echo 'Environment check passed.'
            }
        }

        stage('Run Tests') {
            steps {
                // 对应之前 Build Steps 中的复杂配置
                // dir 步骤会将当前的工作目录切换到你指定的文件夹（如果文件夹不存在，它会自动创建）。
                dir('Appium/MyDemoApp') {
                    script {
                        // 调用刚才写的 bat 脚本
                        // 这样 Jenkinsfile 很干净，具体逻辑在 bat 里改
                        bat 'run_tests.bat'
                    }
                }
            }
        }
    }

    // 对应 Freestyle 的 Post-build Actions
    post {
        always {
            echo '构建结束，正在处理报告...'

            // 1. 生成 Allure 报告
            // path: 必须填 json 数据所在的相对路径
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'Appium/MyDemoApp/report']]

            // 2. 归档日志文件 (方便在 Jenkins 网页直接下载)
            // allowEmptyArchive: true 防止没生成日志时报错
            archiveArtifacts artifacts: 'Appium/MyDemoApp/logs/*.log', allowEmptyArchive: true
        }

        success {
            echo '✅ 测试通过！'
            // 这里可以加发送邮件/钉钉通知的代码
        }

        failure {
            echo '❌ 测试失败！'
            // 这里可以加发送报警通知的代码
        }
    }
}