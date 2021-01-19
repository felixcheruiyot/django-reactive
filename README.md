# Django Reactive - Not to be confused by React

[Hotwire](https://hotwire.dev/) brings a lot of hope to teams that wants to move fast by developing and deploying applications without separating the backend (API) and the frontend (SPA). A single developer can make use of Django simplicity and ship faster. Although Hotwire somehow leads the way in what seems to be a NO-SPA movement, I find its approach not fit for me as a Django developer. 

### Here is why:

Hotwire relies mostly on streams to update UI. This means for every project it is mandatory to have Django channels or something similar. This basically introduces complexity in projects expecially in a case where I might not need websockets in anything else rather than updating the UI.

## Django reactive approach

My approach is to use already existing resources from Javascript ecosystem and refactor how Jinja templating is done. This way, the developer doesn't have to change the existing code much but it simply compile your template into Javascript. Then we use Javascript Dom events and store manager (Redux) to maintain states.

Generally you get to write Django code as usual but the result template is rendered as javascript, and that way we can make it reactive such as in React and VueJS.

Summary: Django reactive proposes compiling template to javascript objects for easy data states management and rendering using the same principles used in SPA frameworks.

NB: This project is at very early stage - consider hiting the watch button or bookmark it for easy tracking of its project. Follow me on https://twitter.com/felixcheruiyot
