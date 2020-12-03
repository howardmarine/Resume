"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = '<p>Experienced data enthusiast with a proven ability of analyzing information to optimize revenue, increase operational efficiencies and assist with strategic planning. Resourceful self-starter, who excels at creating dashboards, comparing forecasts and developing business trends. Creative problem solver with a comprehension of complex issues; expert in distilling random data into meaningful formats and predictions. Applies best in class machine learning techniques to solve the business problems at hand. Prepared to exceed expectations in data discovery, developing and deploying analytics.'
languages = [
        ['English', ' (Native)'],
        ['Russian', ' (Native)'],
        ['Armenian', ' (Proffesional)']
        ]

education = [
        ['BS in Applied and Computational Math Sciences', 'University of Washington', '2010 - 2013'],
        ['AA in Business Intelligence', 'Bellevue College', '2008 - 2010']
        ]

interests = ['Climbing', 'Snowboarding', 'Cooking']

skills = [
        ['Python & Django', '98%'],
        ['Javascript & jQuery', '98%'],
        ['Angular', '98%'],
        ['HTML5 & CSS', '95%'],
        ['Ruby on Rails', '85%'],
        ['Sketch & Photoshop', '60%']
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']
The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Full Stack Developer',
            '2020 - Present',
            'Force Tracker, San Diego',
            '<p>Developed a web application that tabs on everything that happens with the workforce and automates employee or contractor payment without the burden of paperwork. It merges the latest technology with website applications to help decision making based on reliable and detailed data. It determines the exact location of your workforce and subcontractors to a specific job site resulting in full awareness of your operations.  Force Tracker tracks all employees on a digital map and provides the critical knowledge to maintain employees’ job sites. Furthermore, it evaluates individual’s to projects for an efficient decision process with low operating costs.<p>Developed Force Tracker to account for job hours and safe payment automation over Dwolla platform all in one place. Force Tracker is an application to manage workforce and their payment methods.</p><p>Developed database tables and stored procedures using SQL Server to be used in conjunction with .NET. </p><p>Created SQL stored procedures, tables, models, services, and controllers to create API endpoints and implement backend logic for different features within the application.</p><p>Designed front-end components using JavaScript, React, and Bootstrap resulting in dynamic, user-friendly features so that they could be reused in other areas of the application. </p>'
        ],
        ['Data Scientist',
            '2018 - 2020',
            'San Diego',
            '<p>Describe your role here lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.</p>'
        ],
        ['Modeling Analyst',
            '2012 - 2014',
            'Starbucks, Seattle',
            '<p>Describe your role here lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.</p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>You can list your side projects or open source libraries in this section. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>'
projects = [
        ['Velocity',
            'A responsive website template designed to help startups promote, market and sell their products.',
            '#hook'
        ],
        ['DevStudio',
            'A responsive website template designed to help startups promote, market and sell their products.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-web-development-agencies-devstudio/'
        ],
        ['Tempo',
            'A responsive website template designed to help startups promote their products or services and to attract users &amp; investors.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-startups-tempo/'
        ],
        ['Atom',
            'A comprehensive website template solution for startups/developers to market their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/'
        ],
        ['Delta',
            'A responsive Bootstrap one page theme designed to help app developers promote their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-mobile-apps-delta/'
        ]
    ]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
data = {
    'site_title' : 'Responsive Resume/CV Template for Developers',
    'name' : 'Marine Howard',
    'tagline' : 'Full Stack Developer',
    'email' : 'alegar3507@yahoo.com',
    'phone' : '425-753-7908',
    'website' : 'portfoliosite.com',
    'linkedin' : 'linkedin.com/in/marinehoward',
    'github' : 'github.com/howardmarine',
    'twitter' : '@twittername',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    'project_intro' : project_intro,
    'projects' : projects
    }