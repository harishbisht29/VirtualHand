# Virtual-Hand 

Program which records Mouse and Keyboard movements. Recorded movements can be played again. 


## Usage
Just run record.py file using 
```
python record.py
```
It will record mouse movements and keyboard strokes and store them in mouse and keyboard plain files respectively.
The recording looks like this
![](screenshots/mouse.png)

Lets pick one entry to understand its meaning.
M_MM_(586,0)__155091310.6810498 -- 
M_MM - Starting M shows its a mouse movement.Second and third MM shoes Mouse Movement followed by coordinates. Trailing decimal number is used to find find.

To replay the actions recorded, execute the below command
```
python Testing.py
```
## Output
Record 

![](screenshots/virtual_hand_record.gif)

Replay

![](screenshots/virtual_hand_replay.gif)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Inspiration

* Sole inpiration of this code is my LAZINESS to perform repetative tasks.

![](https://media.giphy.com/media/pVkmGyqYRt4qY/giphy.gif)
