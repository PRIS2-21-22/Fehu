## Mejora del producto software. Refactoring

### Code Review.
In this section, we be explain the steps to make a code review.
In the first place, we are going to use two tools.
SonarCloud and Codacy.

SonarCloud is a powerfull tool, here, we can observe a good overview of the code. This tool provide us with information of the bugs and how fix it as the code smells and their solutions.

![Imagen SonarCloud](/images/sonarCloud.png)

SonarCloud has a section with the issues, here we can see one of the issues in the last analysis. 

![Imagen SonarCloud Issue](/images/sonarCloudIssue.png)

For using Codacy after the link is established, we can search in the dashboard for looking the quality evolution as in SonarCloud, also, codacy share with us more information about complexity, duplication and coverage.

![Imagen Codacy](/images/codacy.png)

In the issue section, a lot of information may appear, but it is not neccesary fix everything if you are sure that this could be a false positive.

![Imagen Codacy Issues](/images/codacyIssue.png)

Codacy allow us to make comments directly in Github, this is a faster way for notify our partners if there is a problem in the code.

![Imagen comentarios](/images/Comentarios.png)

The second step after presenting the tools, will be how we can share all the information to help our partner to improve the code.

The best way to comunicate issues is using the issues from github itself. We can see this example below where it can be found some of the more relevant issues found by me.
Also, here is the link: https://github.com/PRIS2/uruz/issues

![Imagen issues](/images/issues.png)


Another way of comunicate anything, could be with the tool, here there is an example where i make comments to my partner and also, change the priority or the assignment.

![Imagen sonarCloud code smells](/images/SonarCloudCodeSmell.png)

In the case of Codacy, the easiest way of share the issues is by using the comments as we have seen before.

### Refactoring.

When our partner is done with the code review, it is the moment to refactor, in my case, i had to do a few changes. Most of then, relate with names and also fix a few bugs.
Once the refactor is done, it is time to make a new version, v2.0. 

![Imagen release](/images/release.png)

And close all the issues with an appropiate explanation.

Finally, a good way to show all the work can be Github pages. Here is the result of all the work, this index can be found in the branch gh-pages of the Fehu repository.

Aarón Blanco Álvarez
