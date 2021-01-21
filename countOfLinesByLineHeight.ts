private calculateChoiceSliceCount (choices: any[]): number {
    const maxAllowedHeight = 350
    const oneBlockMinHeight = 41.59
    const newRowAdditionalHeight = 20
    const rowMaximumSymbols = 35

    function getSpaceIndexInText (text: string): number {
      if (text.length < rowMaximumSymbols || !text.includes(' ')) {
        return -1
      }
      if (text.slice(0, rowMaximumSymbols).includes(' ')) {
        for (let i = rowMaximumSymbols - 1; i > 0; i--) {
          if (text[i] === ' ') {
            return i
          }
        }
      } else {
        for (let i = rowMaximumSymbols - 1; i < text.length; i++) {
          if (text[i] === ' ') {
            return i
          }
        }
      }
      return -1
    }
    function getCountOfLines (text: string) {
      text = text.trim()
      let countOfLines = 0

      while (text) {
        countOfLines++

        const spaceIndex = getSpaceIndexInText(text)

        console.log('string ', text.slice(0, spaceIndex))

        if (spaceIndex < 0) {
          break
        }

        text = text.slice(spaceIndex + 1).trim()
      }

      return countOfLines
    }

    const choicesHeight = choices.map(choice =>
      (getCountOfLines(choice.text.text_lang) - 1) * newRowAdditionalHeight + oneBlockMinHeight
    )

    let countOfAllowedBlocks = 0
    let sumOfBlockHeight = 0

    while (sumOfBlockHeight < maxAllowedHeight) {
      sumOfBlockHeight += choicesHeight[countOfAllowedBlocks]
      countOfAllowedBlocks++
    }

    console.error(countOfAllowedBlocks, sumOfBlockHeight)

    return countOfAllowedBlocks
  }
