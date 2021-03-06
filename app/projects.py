class SiteData:

    lang_dict = {
        'C++': 'image/langs/cpp-logo.png',
        'Python': 'image/langs/python-logo.jpg',
        'Go': 'image/langs/go-logo.png',
        'PL/pgSQL': 'image/langs/plpgsql.png'
    }

    projects = [
        {
            'name': 'web-testing-tool',
            'image': lang_dict['Python'],
            'front_description': 'Students testing tool.',
            'back_description': 'Testing tool implemented on Django. Data storage is implemented in the DBMS MongoDB.',
            'tags': [
                'web',
                'python',
                'html5',
                'js',
                'bootstrap4',
                'django',
                'rest api'
                'mongo',
                'docker',
                'travis ci',
                'github actions'
            ],
            'github_name': 'web-testing-tool',
        },
        {
            'name': 'video-tracker',
            'image': lang_dict['C++'],
            'front_description': 'Detecting and tracking objects on video with OpenCV usage.',
            'back_description': 'Application for tracking various objects and estimating their speed in video stream.',
            'tags': [
                'c++17',
                'computer vision',
                'ml',
                'cmake',
                'opencv',
                'dlib',
                'mobile net ssd',
                'video detection',
                'video tracking'
            ],
            'github_name': 'video-tracker',
        },
        {
            'name': 'smart-text-editor',
            'image': lang_dict['Python'],
            'front_description': 'Text editor with intelligent typing based on relevant search in Elasticsearch.',
            'back_description': 'Web application for editing text documents with support for intelligent typing ' +
                                'based on relevant search in Elasticsearch.',
            'tags': [
                'web',
                'python',
                'flask',
                'rest api',
                'elasticsearch',
                'docker',
                'travis ci',
                'github actions'
            ],
            'github_name': 'smart-text-editor'
        },
        {
            'name': 'vk-news-dashboard',
            'image': lang_dict['Python'],
            'front_description': 'Simple dashboard for vk news groups.',
            'back_description': 'Simple dashboard implemented on Dash. Provides monitoring VK news groups posts.',
            'tags': [
                'web',
                'python',
                'dash',
                'nlp',
                'postgres',
                'docker',
                'docker compose',
                'travis ci'
            ],
            'github_name': 'vk-news-dashboard',
            'ref': 'http://vknews.vnkrtv.ru/',
        },
        {
            'name': 'vk-tracker',
            'image': lang_dict['Python'],
            'front_description': 'Web app for tracking, analyzing and searching people in VK.',
            'back_description': 'Web app for tracking and searching VK users. ' +
                                'Implemented on django and dash, data is stored in MongoDB and Neo4j. ',
            'tags': [
                'web',
                'python',
                'html5',
                'js',
                'bootstrap4',
                'django',
                'dash',
                'mongo',
                'neo4j',
                'docker',
                'docker compose',
                'travis ci',
                'github actions',
                'vk api'
            ],
            'github_name': 'vk-tracker',
        },
        {
            'name': 'go-vk-news-loader',
            'image': lang_dict['Go'],
            'front_description': 'Service loading news from vk news groups.',
            'back_description': 'Service providing loading news from list of vk news groups into PostgreSQL DB.',
            'tags': [
                'microservice',
                'go',
                'postgres',
                'docker',
                'docker compose',
                'travis ci'
            ],
            'github_name': 'go-vk-news-loader',
        },
        {
            'name': 'telegram-channels-loader',
            'image': lang_dict['Python'],
            'front_description': 'Service providing loading messages from telegram channels.',
            'back_description': 'Service providing loading messages from given telegram channels to PostgreSQL DB.',
            'tags': [
                'microservice',
                'python',
                'telegram',
                'async',
                'postgres',
                'docker',
                'docker compose',
                'travis ci'
            ],
            'github_name': 'telegram-channels-loader',
        },
        {
            'name': 'tiktok-loader',
            'image': lang_dict['Python'],
            'front_description': 'Service loading TikTok information.',
            'back_description': 'Service loading information about russian TikTik popular users. ' +
                                'Loads to DB latest tiktoks with audios and videos.',
            'tags': [
                'microservice',
                'python',
                'tiktok',
                'postgres',
                'docker',
                'docker compose',
                'travis ci'
            ],
            'github_name': 'tiktok-loader',
        },
        {
            'name': 'web-library',
            'image': lang_dict['Python'],
            'front_description': 'Web app for storing and adding translations of various compositions.',
            'back_description': 'App for adding and storing translations of various compositions. ' +
                                'All data stored in PostgreSQL, web app implemented in Django.',
            'tags': [
                'web',
                'python',
                'html5',
                'js',
                'docker',
                'docker compose',
                'travis ci',
                'github actions'
            ],
            'github_name': 'web-library',
        },
        {
            'name': 'go-habr-loader',
            'image': lang_dict['Go'],
            'front_description': 'Utility loading all posts from habr.com.',
            'back_description': 'Utility providing loading all posts from habr.com into PostgreSQL DB.',
            'tags': [
                'utility',
                'go',
                'postgres',
                'docker',
                'travis ci'
            ],
            'github_name': 'go-habr-loader',
            'ref': 'https://www.kaggle.com/leadness/habr-posts/'
        },
        {
            'name': 'postgres-markov-chain',
            'image': lang_dict['PL/pgSQL'],
            'front_description': 'Text generator based on Markov chain.',
            'back_description': 'Text generator based on Markov chain written on pure PL/pgSQL. Providing text ' +
                                'processing, training Markov chain and generating text.',
            'tags': [
                'utility',
                'postgres',
                'plpgsql',
                'nlp',
            ],
            'github_name': 'postgres-markov-chain',
        },
        {
            'name': 'go-wiki-parser',
            'image': lang_dict['Go'],
            'front_description': 'Utility parsing large xml wiki dump into MongoDB',
            'back_description': 'Utility providing parsing large xml wiki dump into MongoDB. Stored each article as ' +
                                'dict of subtopic with list of all references for other articles.',
            'tags': [
                'utility',
                'go',
                'travis ci'
            ],
            'github_name': 'go-wiki-parser',
        },
        {
            'name': 'web-db-manager',
            'image': lang_dict['Python'],
            'front_description': 'Web app for managing specific MS SQL Server DB.',
            'back_description': 'Web application for working with the subject database of the shop stored in MS SQL ' +
                                'Server DB.',
            'tags': [
                'web',
                'python',
                'html5',
                'js',
                'flask',
                'mssql server',
                'travis ci'
            ],
            'github_name': 'web-db-manager',
        },
        {
            'name': 'matrix-multiplier',
            'image': lang_dict['C++'],
            'front_description': 'Calculates all possible products of vectors in a given matrix.',
            'back_description': 'Calculates all possible products of vectors in a given matrix with specified ' +
                                'threshold, preserving the final product chains.',
            'tags': [
                'utility',
                'c++14',
                'libtorch',
                'qt5',
                'map reduce',
                'cmake',
                'cuda'
            ],
            'github_name': 'matrix-multiplier',
        },
        {
            'name': 'cmd-vk-tracker',
            'image': lang_dict['C++'],
            'front_description': 'Console application for Windows providing monitoring VK users.',
            'back_description': 'Console application providing loading VK users information, getting ' +
                                'account changes and users relationship.',
            'tags': [
                'utility',
                'c++14',
                'cmake',
                'vk api'
            ],
            'github_name': 'cmd-vk-tracker',
        },
        {
            'name': 'wifi-detect',
            'image': lang_dict['C++'],
            'front_description': 'Small console application for detecting Wi-Fi routers and connected to them devices.',
            'back_description': 'Detects wifi routers and all devices, connected to them. Also records all captured ' +
                                'traffic in capture.pcap.',
            'tags': [
                'utility',
                'c++14',
                'cmake'
            ],
            'github_name': 'wifi-detect',
        },
        {
            'name': 'tf-net-analizer',
            'image': lang_dict['Python'],
            'front_description': 'Notebooks with NN classifying internet traffic.',
            'back_description': 'Notebooks with NN classifying internet traffic from KDD Cup 1999 data. Implemented '
                                'on TensowFlow.',
            'tags': [
                'data science',
                'ml',
                'python',
                'tensorflow',
                'sklearn',
                'jupyter notebook'
            ],
            'github_name': 'tf-net-analizer',
            'ref': 'https://www.kaggle.com/leadness/knncup99-ffnn-0-96-acc-0-57-weighted-acc'
        },
        {
            'name': 'go-tcp-chat',
            'image': lang_dict['Go'],
            'front_description': 'Simple TCP chat with tui.',
            'back_description': 'Simple TCP chat on sockets with text user interface.',
            'tags': [
                'service',
                'go'
            ],
            'github_name': 'go-tcp-chat'
        },
        {
            'name': 'my-site',
            'image': lang_dict['Python'],
            'front_description': 'This site.',
            'back_description': 'Simple single page site implemented on Flask.',
            'tags': [
                'web',
                'python',
                'html5',
                'bootstrap4',
                'flask'
            ],
            'github_name': 'my-site'
        }
    ]
