# IPRangeAnalyzer

IPRangeAnalyzer is a Python script that analysis ip range.

#### .e.g.

extracts ip range
(`
192.168.0.1-192.168.0.5
`) to 
`192.168.0.1`
`192.168.0.2`
`192.168.0.3`
`192.168.0.4`
`192.168.0.5`
## Installation

clone the repository.

```bash
git clone https://github.com/SinaKzlca/IPRangeAnalyzer
cd IPRangeAnalyzer/
```
ready to go!

## Usage

```bash
python IPRangeAnalyzer.py -ipr [ip range list] -o [output file path]
```
#### .e.g.
```bash
python IPRangeAnalyzer.py -ipr 127.0.0.1-127.0.1.255 192.168.0.1-192.168.0.5 -o output.txt
```
##### If you have large list of the ip ranges you can import ip range list via text file.
```bash
python IPRangeAnalyzer.py -i [input file path] -o [output file path]
```
#### .e.g.
```bash
python IPRangeAnalyzer.py -i ~/Downloads/iprange.txt -o output.txt
```
##### example of input file:
![alt text](https://github.com/SinaKzlca/IPRangeAnalyzer/blob/main/Screenshot%20from%202021-03-18%2016-58-27.png ".e.g input file")


---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
