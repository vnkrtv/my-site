class SiteData:

    carousel_images = [
        'image/carousel/1.jpg',
        'image/carousel/2.jpg',
        'image/carousel/3.jpg'
    ]

    lang_dict = {
        'C++': 'image/langs/cpp-logo.png',
        'Python': 'image/langs/python-logo.jpg',
        'Go': 'image/langs/go-logo.png',
    }

    projects = [
        {
            'name': 'vk-tracker',
            'image': lang_dict['Python'],
            'front_description': 'Web app for tracking, analyzing and searching people in VK.',
            'back_description': 'Web app for tracking and searching VK users. ' +
                                'Implemented on django and dash, data is stored in MongoDB and Neo4j. ',
            'tags': [
                'python',
                'html5',
                'js',
                'bootstrap4',
                'django',
                'dash',
                'mongo',
                'neo4j',
                'docker',
                'travis ci',
                'github actions',
                'vk api'
            ],
            'github_name': 'vk-tracker',
        },
        {
            'name': 'web-testing-tool',
            'image': lang_dict['Python'],
            'front_description': 'Students testing tool.',
            'back_description': 'Testing tool implemented on Django. Data storage is implemented in the DBMS MongoDB.',
            'tags': [
                'python',
                'html5',
                'js',
                'bootstrap4',
                'django',
                'mongo',
                'docker',
                'travis ci',
                'github actions'
            ],
            'github_name': 'web-testing-tool',
        },
        {
            'name': 'vk-news-dashboard',
            'image': lang_dict['Python'],
            'front_description': 'Simple dashboard for vk news groups.',
            'back_description': 'Simple dashboard implemented on Dash. Provides monitoring VK news groups posts.',
            'tags': [
                'python',
                'dash',
                'postgres',
                'docker',
                'travis ci'
            ],
            'github_name': 'vk-news-dashboard',
            'ref': 'http://vknews.vnkrtv.ru/',
        },
        {
            'name': 'go-vk-news-loader',
            'image': lang_dict['Go'],
            'front_description': 'Service loading news from vk news groups.',
            'back_description': 'Service providing loading news from list of vk news groups into PostgreSQL DB.',
            'tags': [
                'go',
                'postgres',
                'docker',
                'travis ci'
            ],
            'github_name': 'go-vk-news-loader',
        },
        {
            'name': 'web-library',
            'image': lang_dict['Python'],
            'front_description': 'Web app for storing and adding translations of various compositions.',
            'back_description': 'App for adding and storing translations of various compositions. ' +
                                'All data stored in PostgreSQL, web app implemented in Django.',
            'tags': [
                'python',
                'html5',
                'js'
                'docker',
                'travis ci',
                'github actions'
            ],
            'github_name': 'web-library',
        },
        {
            'name': 'go-habr-loader',
            'image': lang_dict['Go'],
            'front_description': 'Service loading all posts from habr.com.',
            'back_description': 'Service providing loading all posts from habr.com into PostgreSQL DB.',
            'tags': [
                'go',
                'postgres',
                'docker',
                'travis ci'
            ],
            'github_name': 'go-habr-loader',
            'ref': 'https://www.kaggle.com/leadness/habr-posts/'
        },
        {
            'name': 'go-wiki-parser',
            'image': lang_dict['Go'],
            'front_description': 'Service loading all posts from habr.com.',
            'back_description': 'Utility providing parsing large xml wiki dump into MongoDB. Stored each article as ' +
                                'dict of subtopic with list of all references for other articles.',
            'tags': [
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
                'python',
                'tensorflow',
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
                'python',
                'html5',
                'bootstrap4',
                'flask'
            ],
            'github_name': 'my-site'
        }
    ]
