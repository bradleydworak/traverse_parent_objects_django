traverse_parent_objects_django
==============================

Traversing successive parent object relationships in a single Django call inside a view

Suppose for example your database consists of a collection of articles written by various authors published in numerous newspapers. You need to gather a list of all authors who published in a particular newspaper title called "The Chronicle". This search query/filter requires traversing the author|article|newspaper parent object relationships in Django. Assume you have a model where each Article has a foreign key to a certain newspaper and many-to-many relationships exist from authors to articles. Below is some example code on how to accomplish this.
