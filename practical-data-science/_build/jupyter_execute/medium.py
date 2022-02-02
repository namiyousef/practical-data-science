#!/usr/bin/env python
# coding: utf-8

# # This article was written on Jupyter Notebook
# ## A brief introduction to jupyter-book and jupyter_to_medium

# For the longest time, I've kept notes locally on Apple Pages. To that end, I have no complaints. Pages is an amazing piece of software that allows you to quickly produce high quality documents (with really great diagrams and tables) in a fraction of the time it would take on Overleaf, Word or Google Docs.
# 
# However, there have been a couple of things that have always annoyed me about it:
# - Versionining is not possible
# - The documents cannot be easily shared
# - Documenting code is really hard
# 
# These aren't unique to Pages either. Word, Docs and Overleaf suffer from the same problems for the most part. None of these tools are great for continuously updating shared notes, creating documentation or incorporating code.
# 
# The good news is that I've recently learnt how to use two new Python libraries that are going to help me greatly accelerate my notetaking and article writing. These are `jupyter-book` and `jupyter_to_medium`.
# 
# In this article (which I happen to be writing on a Jupyter Notebook!) I will explain how you can use both tools to accelerate notetaking and writing articles.

# ## What is `jupyter_to_medium`?
# 
# `jupyter_to_medium` is a Python package that allows you to directly deploy your Jupyter Notebook articles to Medium. This is useful if you typically base most of your articles on content from Jupyter Notebooks. I've been curious about this package for a while, but I've only just gotten round to experimenting with it... let's see what it can do! If things go well I may strongly consider using it as the main source of my articles.
# 
# ### Installation
# 
# ### Images
# 
# ### Links
# 
# ### Code

# ## What is `jupyter-book`?
# 
# `jupyter-book` is a package that allows you to easily produce book like documents using markdown files and jupyter notebook files. For this reason, they are extremely flexible, and can allow you to quickly generate rich documents in a really short time. What's more, they can be integrated with GitHub Actions to enable CI/CD behaviour. If you are looking for a quick intallation of `jupyter-book` without any CI/CD features, just run:

# In[1]:


# install jupyter-book
get_ipython().system('pip install jupyter-book')

# create a book
get_ipython().system('jupyter-book create your_book_name')


# This creates a book with the name `your_book_name` if your current working directory. You can add any markdown or notebook files in this directory and then modify the `_toc.yml` file to add them to the structure of your book! It's that easy!
# 
# ### Installation using cookiecutter
# 
# My preferred way of installing `jupyter-book` is through `cookiecutter`. This method comes with extra files that interface with GitHub Actions to enable CI/CD on the project. To install using this method, first make sure you have `cookiecutter` installed:

# In[2]:


# install cookiecutter
get_ipython().system('pip install -U cookiecutter')


# Then, use the following cookiecutter command to download the latest jupyter-book configuration:

# In[3]:


get_ipython().system('cookiecutter git@github.com:executablebooks/cookiecutter-jupyter-book.git')


# This then allows you to add some metadata about your project, such as the title, the author name, the license etc. In particular, I want to bring your attention to `book_slug` and `select include_ci_files`. For the former, it is the name of your project for download purposes, e.g. if you wanted to run `pip install project`. I have not used this feature yet, however I'm mentioning it in case you are interested in learning more about it. See [this](https://github.com/audreyfeldroy/cookiecutter-pypackage/issues/487) GitHub issue for a thread on what a slug is in `cookiecutter`. 
# 
# The more interesting tag is `select include_ci_files`. Selecting 1 will download CI/CD configurations for GitHub (whereas 2 will download that for GitLab). I'll be going through what this does for GitHub.

# ### CI/CD files

# ### Pushing to GitHub

# ### Making Changes

# ### Features

# ## Thoughts and Takeaways
# 
# Personally, I don't usually write my articles from Jupyter Notebooks. I really like the clear split of running expeirments on Jupyter (or usually just Python) and then writing an article with a clear narrative in mind in order to make it appealing to the reader.
# 
# Thoughts on jupyter_to_medium in general?
# 
# So going forward, I don't think I'll be using `jupyter_to_medium` much, if at all.
# 
# On the other hand, `jupyter-book` seems extremely promising. I am quite fond of it so far, and I think I'll start notetaking there as opposed to locally, while slowly starting to migrate my older content.
# 
