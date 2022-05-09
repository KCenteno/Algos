let groupAnagrams = (strs) => {
    let anagrams = {}
    let collectedAnagrams = []
    
    // iterate through strs. 
    for (let word of strs){
        // use the anagrams hash to find & store arrays of anagrams

        // alphabetize letters
        let letters = word.split('').sort().join('')

        // create hash key-value pair for alphabetized letters of word if it does not exist
        anagrams[letters] = anagrams[letters] || []
        
        // add word to value of the key which matches its letters
        anagrams[letters].push(word)
        }
        
    //push those arrays into the collectedAnagrams array
    
      // iterate through anagrams hash keys
    for (let key in anagrams){
     // add their values as subarrays of the collectedAnagrams array
        collectedAnagrams.push(anagrams[key])
    }

    // return the array of arrays
    return collectedAnagrams
}

console.log(groupAnagrams(["rat", "tar", "art"]))


