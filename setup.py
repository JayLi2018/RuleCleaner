from setuptools import setup, find_packages
  
setup(
    name='Rbbm',
    version='0.0.2',
    url='author.com',
    author='Chenjie Li',
    author_email='cli112@hawk.iit.edu',
    description='RuleCleaner source code',
    packages=find_packages(),
    install_requires=["colorful",
                    "gensim",
                    "ipython",
                    "lark",
                    "lime",
                    "matplotlib",
                    "names",
                    "networkx",
                    "nltk",
                    "numpy",
                    "pandas",
                    "psycopg2_binary",
                    "pyitlib",
                    "pytest",
                    "python_Levenshtein",
                    "requests",
                    "setuptools",
                    "SQLAlchemy",
                    "textblob",
                    "torch",
                    "tqdm",
                    "transformers"],
    entry_points={
        'console_scripts': [
            'rbbm=rbbm_src.main:main',
        ]},
    )