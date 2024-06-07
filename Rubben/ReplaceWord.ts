function replaceWords(dictionary: string[], sentence: string): string {
    let word = sentence.split(" ")
    let dictSet = new Set<string>(dictionary)
    function find_root(word: string, dictSet: Set<string>): string {
        for(let i = 0; i < word.length; i++) {
            let root: string = word.substring(0, i)
            if(dictSet.has(root)) {
                return root
            }
        }
        return word
    }
    for(let i = 0; i < word.length; i++) {
        word[i] = find_root(word[i], dictSet)
    }
    return word.join(" ")
}