from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

class Dictionary:
    def get_definition(self, word):
        """Get definitions from WordNet"""
        synsets = wordnet.synsets(word)
        if not synsets:
            return f"No definition found for '{word}'"
        
        results = []
        for syn in synsets[:3]:  # Limit to 3 definitions
            definition = syn.definition()
            examples = ", ".join(syn.examples()[:2]) if syn.examples() else ""
            results.append(f"• {definition}" + (f"\n  Examples: {examples}" if examples else ""))
        
        return "\n\n".join(results)
    
    def extract_word(self, query):
        """Extract word to define"""
        return query.lower().replace("define", "").strip()