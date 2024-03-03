function Extract_Substring(input: string, start: string, end:string): string | null {
    let start_ind: number = input.indexOf(start);
    let end_ind: number = input.indexOf(end);

    console.log("Extract called");
    if (start_ind !== -1) {
        if (end_ind !== -1) {
            let output = input.substring(start_ind, end_ind + end.length)
            return output
        }
    }

    console.log("ERROR: start/end could not be found in Parse");
    return null;
}
export function Parse(input: string) {
    let test_input: string = `Here is JSON: [
        {
          "front": "When did the American Revolution take place?",
          "back": "The American Revolution took place from 1765 to 1783."
        },
        {
          "front": "What were some of the key events in the American Revolution?",
          "back": "Key events such as the Boston Tea Party in 1773 and the signing of the Declaration of Independence in 1776 were pivotal moments in the revolution."
        },
        {
          "front": "When did the war of the American Revolution officially begin and what marked this beginning?",
          "back": "The war itself officially began in 1775 with the Battles of Lexington and Concord, marking the first military engagements between the colonies and Britain."
        },
        {
          "front": "Who were some notable figures in the American Revolution?",
          "back": "Notable figures like George Washington, Thomas Jefferson, and Benjamin Franklin played crucial roles in leading the revolution and shaping its outcome."
        },
        {
          "front": "What ended the American Revolution and what did it establish?",
          "back": "The Treaty of Paris in 1783 formally ended the war, recognizing the United States as an independent nation and establishing its borders."
        }
      ] `
    const json_string = Extract_Substring(test_input, "[", "]");
    if (json_string !== null) {
        let output = JSON.parse(json_string);
        //console.log(output)
        //console.log(output[0]["front"])
        return output;
    }
    ///console.log("Parse retuning");
    //console.log(JSON);
    
    console.log("ERROR: Parse failed")
    return null;
}