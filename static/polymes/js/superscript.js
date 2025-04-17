/**
 * Converts caret notation (e.g., 10^6) to Unicode superscripts (e.g., 10⁶)
 * For display in the PolymDB application
 */
document.addEventListener('DOMContentLoaded', function() {
  // Find elements containing text in the entire document
  // Most comprehensive selector to catch all possible text-containing elements
  const elements = document.querySelectorAll('*');
  
  // Mapping of regular characters to their Unicode superscript equivalents
  const superscriptMap = {
    // Numbers
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    
    // Symbols
    '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
    
    // Lowercase letters
    'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 
    'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
    'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ',
    'p': 'ᵖ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ',
    'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
    
    // Uppercase letters (limited availability in Unicode)
    'A': 'ᴬ', 'B': 'ᴮ', 'D': 'ᴰ', 'E': 'ᴱ', 'G': 'ᴳ',
    'H': 'ᴴ', 'I': 'ᴵ', 'J': 'ᴶ', 'K': 'ᴷ', 'L': 'ᴸ',
    'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ', 'R': 'ᴿ',
    'T': 'ᵀ', 'U': 'ᵁ', 'V': 'ⱽ', 'W': 'ᵂ'
  };
  
  // Function to process text nodes
  function processTextNode(textNode) {
    const text = textNode.nodeValue;
    
    // Skip empty nodes and nodes without the caret symbol
    if (!text || !text.includes('^')) return;
    
    // Use regex to find all instances of caret notation
    const newText = text.replace(/(\S+)\^(\S+)/g, function(match, base, exp) {
      let superscript = '';
      
      for (let i = 0; i < exp.length; i++) {
        const char = exp[i];
        if (superscriptMap[char]) {
          superscript += superscriptMap[char];
        } else if (char.toUpperCase() === char && /[A-Z]/.test(char)) {
          // For uppercase letters without Unicode superscripts, we keep them as is
          // since we can't add HTML tags to text nodes
          superscript += char;
        } else {
          superscript += char;
        }
      }
      
      return base + superscript;
    });
    
    if (text !== newText) {
      textNode.nodeValue = newText;
    }
  }
  
  // Process all text nodes in the document
  function walkTextNodes(node) {
    if (node.nodeType === 3) { // Text node
      processTextNode(node);
      return;
    }
    
    // Skip script and style elements
    if (node.tagName === 'SCRIPT' || node.tagName === 'STYLE') {
      return;
    }
    
    // Process child nodes
    const children = node.childNodes;
    for (let i = 0; i < children.length; i++) {
      walkTextNodes(children[i]);
    }
  }
  
  // Start processing from the body
  walkTextNodes(document.body);
  
  // Also handle HTML content for more complex cases
  elements.forEach(function(element) {
    // Skip certain elements
    if (element.tagName === 'SCRIPT' || element.tagName === 'STYLE' || 
        element.tagName === 'TEXTAREA' || element.tagName === 'INPUT') {
      return;
    }
    
    if (element.innerHTML && element.innerHTML.includes('^')) {
      const html = element.innerHTML;
      
      // More specific pattern to catch cases like (T7^rep-7)
      const newHtml = html.replace(/\b([A-Za-z0-9]+)\^([A-Za-z0-9\-]+)\b/g, function(match, base, exp) {
        let superscript = '';
        
        for (let i = 0; i < exp.length; i++) {
          const char = exp[i];
          if (superscriptMap[char]) {
            superscript += superscriptMap[char];
          } else if (char.toUpperCase() === char && /[A-Z]/.test(char)) {
            superscript += '<sup>' + char + '</sup>';
          } else {
            superscript += char;
          }
        }
        
        return base + superscript;
      });
      
      if (html !== newHtml) {
        element.innerHTML = newHtml;
      }
    }
  });
});
