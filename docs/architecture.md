# PIC Architecture: The Interceptor Pattern



```mermaid
graph TD
    User[User Input / External Webhook] -->|Untrusted| Agent[AI Agent / Planner]
    Agent -->|Generates| Proposal[PIC Action Proposal]
    
    subgraph PIC_Governance_Layer
        Proposal --> Verifier[PIC Verifier Middleware]
        Checker[Evidence Checker] -->|Verify Hashes/API| Verifier
        TrustDB[(Trusted Sources / PGP Keys)] --> Checker
    end
    
    Verifier -->|Validation Failed| Block[Blocked & Logged]
    Verifier -->|Validation Passed| Executor[Tool Executor / API]
    Executor -->|Side Effect| Success[Success]
