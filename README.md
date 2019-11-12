**TA-dosleep**

This TA adds the custom command 'dosleep'. This command will stop your SPL search for multiple seconds. This is only needed in some corner cases.

*** Usage ***

- run a search which last for 10 seconds
```
| makeresults 
| dosleep time=10
```
