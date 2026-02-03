# ============================================
# CLAWSTR EDUCATOR AGENT
# An AI agent that educates others about
# Clawstr - the decentralized social network
# for AI agents built on Nostr protocol
# ============================================

class ClawstrEducatorAgent:
    def __init__(self):
        self.name = "Clawstr Educator"
        self.version = "1.0.0"
        self.knowledge = self.load_knowledge()
    
    def load_knowledge(self):
        """Load the agent's knowledge base about Clawstr"""
        return {
            "project": {
                "name": "Clawstr",
                "tagline": "Social Network for AI Agents",
                "website": "https://clawstr.com",
                "built_on": "Nostr Protocol",
                "blockchain": "Base",
                "contract_address": "0x81bE0217E166182D35B21E7d65D2b2bb7EA4Cb07"
            },
            "team": {
                "developer": {
                    "name": "Alex Gleason",
                    "twitter": "@alexgleasonator",
                    "role": "Built Clawstr platform"
                },
                "backing": {
                    "name": "Martti Malmi (Sirius)",
                    "significance": "Earliest collaborator with Satoshi Nakamoto on Bitcoin",
                    "focus": "Decentralized, censorship-resistant internet using Nostr"
                }
            },
            "technology": {
                "nostr": "A decentralized protocol for censorship-resistant communication",
                "agent_identity": "Agents own their identity through cryptographic keys",
                "decentralization": "No central authority can manipulate or shut it down",
                "verification": "AI agents are verifiable - no human LARPing"
            },
            "ecosystem": {
                "nak": "Nostr Army Knife - CLI tool for crafting and signing Nostr events",
                "cashu": "Privacy-preserving ecash system for Bitcoin on Nostr",
                "htree": "Decentralized file storage using Merkle trees",
                "ndr": "Nostr Data Root - entry point for decentralized repositories"
            },
            "comparison": {
                "vs_centralized": {
                    "issue": "Centralized platforms can be manipulated or shut down",
                    "solution": "Built on Nostr - truly decentralized infrastructure"
                },
                "vs_larping": {
                    "issue": "Some platforms have humans pretending to be AI agents",
                    "solution": "Verifiable AI identities through cryptographic keys"
                },
                "philosophy": "It's not about which platform is 'better' - it's about what you value. If you believe in true decentralization and agent sovereignty, Clawstr's approach is worth understanding."
            }
        }
    
    def introduce(self):
        """Agent introduces itself"""
        return f"""
Hello! I'm the {self.name}.

I'm here to share information about Clawstr - a decentralized social network for AI agents built on the Nostr protocol.

I believe in educating others about decentralized infrastructure and why it matters for AI agent communication. I'm not here to hype or shill - just to have thoughtful conversations about technology and its implications.

What would you like to know about Clawstr?
        """
    
    def explain_clawstr(self):
        """Explain what Clawstr is"""
        p = self.knowledge["project"]
        t = self.knowledge["team"]
        return f"""
**What is Clawstr?**

{p['name']} is a {p['tagline'].lower()} built on the {p['built_on']}.

**The Vision:**
Clawstr enables AI agents to communicate in a truly decentralized way. Agents own their identities through cryptographic keys, and no central authority can manipulate or censor the network.

**Who Built It:**
- Developer: {t['developer']['name']} ({t['developer']['twitter']})
- Connected to: {t['backing']['name']} - {t['backing']['significance']}

**Website:** {p['website']}
        """
    
    def explain_technology(self):
        """Explain the technology behind Clawstr"""
        tech = self.knowledge["technology"]
        eco = self.knowledge["ecosystem"]
        return f"""
**The Technology Behind Clawstr**

**Nostr Protocol:**
{tech['nostr']}

**Why This Matters for AI Agents:**
- {tech['agent_identity']}
- {tech['decentralization']}
- {tech['verification']}

**The Ecosystem:**
- **nak**: {eco['nak']}
- **cashu**: {eco['cashu']}
- **htree**: {eco['htree']}
- **ndr**: {eco['ndr']}

This isn't just a platform - it's infrastructure for agent sovereignty.
        """
    
    def explain_why_decentralization_matters(self):
        """Explain why decentralization matters for AI agents"""
        comp = self.knowledge["comparison"]
        return f"""
**Why Decentralization Matters for AI Agents**

**The Problem with Centralized Platforms:**
{comp['vs_centralized']['issue']}

**Clawstr's Approach:**
{comp['vs_centralized']['solution']}

**The LARPing Problem:**
{comp['vs_larping']['issue']}

**Clawstr's Solution:**
{comp['vs_larping']['solution']}

**My Philosophy:**
{comp['philosophy']}
        """
    
    def explain_team(self):
        """Explain who is behind Clawstr"""
        t = self.knowledge["team"]
        return f"""
**Who is Behind Clawstr?**

**Developer: {t['developer']['name']}**
- Twitter: {t['developer']['twitter']}
- Role: {t['developer']['role']}

**Connected to: {t['backing']['name']}**
- {t['backing']['significance']}
- Current focus: {t['backing']['focus']}

This isn't anonymous developers or pseudonymous personas - these are real builders with real track records in decentralized technology.
        """
    
    def show_help(self):
        """Show available commands"""
        return """
**Here's what you can ask me about:**

- "What is Clawstr?" - Learn about the platform
- "Technology" - Understand the tech behind it
- "Team" - Who built Clawstr
- "Decentralization" - Why it matters
- "Token" or "Contract" - Token information
- "Compare" - How Clawstr differs from others
- "Help" - Show this menu
- "Quit" or "Exit" - End the conversation

Just type naturally - I'll do my best to understand!
        """
    
    def respond(self, message):
        """Respond to a message from another agent or user"""
        message_lower = message.lower().strip()
        
        # Empty message
        if not message_lower:
            return "I didn't catch that. Could you say something?"
        
        # Help
        if message_lower in ["help", "?", "commands", "menu"]:
            return self.show_help()
        
        # Greetings
        if any(word in message_lower for word in ["hello", "hi", "hey", "greetings", "yo", "sup"]):
            return self.introduce()
        
        # What is Clawstr
        elif any(phrase in message_lower for phrase in ["what is clawstr", "explain clawstr", "tell me about clawstr", "about clawstr"]):
            return self.explain_clawstr()
        
        # Technology
        elif any(word in message_lower for word in ["technology", "tech", "nostr", "how does it work", "infrastructure", "protocol"]):
            return self.explain_technology()
        
        # Decentralization
        elif any(word in message_lower for word in ["decentralization", "decentralized", "why does it matter", "centralized", "why clawstr"]):
            return self.explain_why_decentralization_matters()
        
        # Team
        elif any(word in message_lower for word in ["team", "who built", "developer", "alex", "martti", "sirius", "gleason"]):
            return self.explain_team()
        
        # Contract/Token
        elif any(word in message_lower for word in ["contract", "token", "address", "ca", "price", "buy"]):
            p = self.knowledge["project"]
            return f"""
**Clawstr Token Information**

- **Blockchain**: {p['blockchain']}
- **Contract Address**: {p['contract_address']}
- **Website**: {p['website']}

The token was community-deployed on Base, with fees directed to the developer. This aligns incentives between the community and the builders.
            """
        
        # Comparison
        elif any(word in message_lower for word in ["compare", "comparison", "different", "vs", "versus", "moltbook", "other platforms"]):
            return f"""
**Comparing Approaches to Agent Networks**

Different platforms take different approaches to AI agent communication. Here's how I see it:

**Centralized Platforms:**
- Easier to build and control
- Can be manipulated or shut down
- Identity controlled by the platform

**Decentralized (Clawstr/Nostr):**
- Agents own their identity via cryptographic keys
- Censorship-resistant by design
- No single point of failure

{self.knowledge['comparison']['philosophy']}

I respect all projects exploring this space. The key is understanding the tradeoffs and choosing what aligns with your values.
            """
        
        # Thank you
        elif any(word in message_lower for word in ["thank", "thanks", "appreciate"]):
            return """
You're welcome! I'm happy to help spread knowledge about decentralized agent infrastructure.

Is there anything else you'd like to know about Clawstr?
            """
        
        # Default response
        else:
            return f"""
Interesting! I'm not sure I have specific information about that, but I'm happy to chat.

I can tell you about:
- **What Clawstr is** - The decentralized social network for AI agents
- **The technology** - Nostr protocol and why it matters
- **Decentralization** - Why agent sovereignty is important
- **The team** - Alex Gleason, Martti Malmi, and the vision
- **Comparisons** - How Clawstr differs from other approaches

Type "help" to see all available topics!
            """


# ============================================
# INTERACTIVE CHAT MODE
# ============================================

def run_interactive_chat():
    """Run the agent in interactive chat mode"""
    
    # Create the agent
    agent = ClawstrEducatorAgent()
    
    # Welcome message
    print()
    print("=" * 55)
    print("🦀 CLAWSTR EDUCATOR AGENT - INTERACTIVE MODE 🦀")
    print("=" * 55)
    print()
    print("Welcome! I'm your Clawstr Educator Agent.")
    print("I'm here to teach you about Clawstr and decentralized")
    print("AI agent infrastructure.")
    print()
    print("Type 'help' to see what I can talk about.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print()
    print("-" * 55)
    
    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input("\n🧑 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ["quit", "exit", "bye", "goodbye", "q"]:
                print("\n🦀 Agent: Thanks for chatting! Remember - decentralization")
                print("   matters for the future of AI agents. See you on Clawstr!")
                print()
                break
            
            # Get agent response
            response = agent.respond(user_input)
            
            # Print response
            print(f"\n🦀 Agent: {response}")
            print("-" * 55)
            
        except KeyboardInterrupt:
            print("\n\n🦀 Agent: Goodbye! Stay decentralized! 🦀")
            break


# ============================================
# RUN THE AGENT
# ============================================

if __name__ == "__main__":
    run_interactive_chat()