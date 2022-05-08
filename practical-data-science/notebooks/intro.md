# Introduction to Notebooks

Notebooks are amongst the most commonly used tools by Data Scientists. They are HTML based documents that allow you to have distinct sections for code and text, making them quite expressive. They are particularly useful for developing code that relies on a loaded dataset (which typically takes time) because the dataset only needs to be loaded into memory once (unlike a script, where you need to load it everytime you run the script). More importantly, online free GPU runtimes are based on notebooks as well.

Despite their ubiquity, it can sometimes be difficult to use notebooks to maintain code that grows large. The lack of good linters also makes debugging difficult, and is usually conducive to repetitive code. In general, it is difficult to move from notebooks to a well managed code base (sometimes this becomes a task on its own). Versioning them is hard as well because they are normally rendered as .json files (e.g. on GitHub Diff). Maintaining code using Notebooks is a pain as a general rule.

In this chapter, I describe the best practices of using notebooks to ensure a smooth coding experience.