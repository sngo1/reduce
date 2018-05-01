
var test = "hi there this here sentence is the test sentence so it is here so that there is a sentence for testing".split(" ")
//console.log(test)

var x = [1, 2, 3, 4]
var a = x.reduce(function(a, b) {return a + b})

//console.log(a);

//in Python...
/*def counter(word, file):
    list = [1 for x in file if x == word]
    if list == []:
        return 0
    return reduce ((lambda x, y: x + y), list)*/

//in Javascript...
var frequency = function(word, file){
  var total = [];
  for (x in file){
    if (file[x] == word){
      total.push(1);
    }
  }
  if (total.length == 0){
      return 0;
  }
  return total.reduce(function (x, y) {return x + y})
}
//console.log(test)
console.log(frequency("sentence", test))

/*In Python...
def frequencyOfGroup(word_list):
    freq = 0;
    print "GROUP FREQ: ", [counter(x, contents) for x in word_list]
*/

//In JS...
var freqOfPhrase = function(word_list, file){
  var freqCount = []
  for (x in word_list){
    freqCount.push(frequency(word_list[x], file))
  }
  return freqCount.reduce(function(x,y) {return x + y})
}

console.log(freqOfPhrase(["is", "sentence"], test))

/*In Python...
def mostFrequent(file):
    wordfreq = [(counter(x, file), x) for x in file]
    return "Most Frequent Word: '" + max(wordfreq)[1] + "' appears " + str(max(wordfreq)[0]) + " times."
*/

//In JS...
var mostFrequent = function(file){
  var currentFreq = [];
  for (x in file){
    console.log(file[x])
    currentFreq.push(frequency(file[x]), file);
  }
  var index = Math.max(currentFreq)
  return "Word: " + file[index] + " frequency: " + currentFreq[index];
}

console.log(mostFrequent(test))
