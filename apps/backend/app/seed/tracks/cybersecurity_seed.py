"""
Cybersecurity & Ethical Hacking Track Seed Data
Levels 1 - 6 covering:
- Level 1: Security Foundations & Cryptography
- Level 2: Network Security, Protocols & Packet Inspection
- Level 3: Linux Security & System Hardening
- Level 4: Web Application Security & OWASP Top 10
- Level 5: Defensive Security, SIEM & Incident Response
- Level 6: Advanced Security Engineering, Cloud & Zero Trust
"""

COURSES_DATA = [
    {
        "id": "course-cyber-lvl1",
        "title": "Cybersecurity Level 1: Security Foundations & Cryptography",
        "slug": "cybersecurity-level-1-foundations",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "Master the CIA Triad, threat modeling (STRIDE), symmetric/asymmetric cryptography, and cryptographic hash functions.",
        "category": "Applied Cryptography",
        "level": "beginner",
        "estimated_hours": 14,
        "thumbnail_url": "/assets/courses/cyber-foundations.png",
        "modules": [
            {
                "id": "mod-cyber-1-1",
                "title": "Module 1: The CIA Triad & Threat Modeling",
                "description": "Confidentiality, Integrity, Availability, STRIDE threat models, and Attack Trees.",
                "order": 1,
                "lesson_ids": ["cyber-cia-triad-threat-modeling", "cyber-auth-authorization-access-control"]
            },
            {
                "id": "mod-cyber-1-2",
                "title": "Module 2: Symmetric & Asymmetric Encryption",
                "description": "AES-GCM authenticated encryption, RSA key generation, and Diffie-Hellman key exchanges.",
                "order": 2,
                "lesson_ids": ["cyber-symmetric-asymmetric-encryption", "cyber-sha256-hashing-digital-signatures"]
            }
        ]
    },
    {
        "id": "course-cyber-lvl2",
        "title": "Cybersecurity Level 2: Network Security & Packet Analysis",
        "slug": "cybersecurity-level-2-networking",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "Deep dive into OSI layers, TCP/UDP packet structures, ARP spoofing, Firewalls, Nmap scanning, and Wireshark inspection.",
        "category": "Network Security",
        "level": "intermediate",
        "estimated_hours": 16,
        "thumbnail_url": "/assets/courses/cyber-networking.png",
        "modules": [
            {
                "id": "mod-cyber-2-1",
                "title": "Module 1: TCP/IP Architecture & Protocol Vulnerabilities",
                "description": "TCP 3-way handshake, SYN flood attacks, DNS spoofing, and ARP poisoning.",
                "order": 1,
                "lesson_ids": ["cyber-tcp-handshake-syn-floods", "cyber-dns-arp-spoofing-attacks"]
            },
            {
                "id": "mod-cyber-2-2",
                "title": "Module 2: Network Probing & Wireshark Packet Inspection",
                "description": "Nmap stealth SYN scans, stateful firewall rule enforcement, and deep packet inspection.",
                "order": 2,
                "lesson_ids": ["cyber-nmap-port-scanning-firewalls", "cyber-wireshark-packet-analysis"]
            }
        ]
    },
    {
        "id": "course-cyber-lvl3",
        "title": "Cybersecurity Level 3: Linux Security & System Hardening",
        "slug": "cybersecurity-level-3-linux",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "Linux permissions, SUID binaries, SSH key hardening, process isolation, and bash security automation.",
        "category": "Threat Hunting & Zero Trust",
        "level": "intermediate",
        "estimated_hours": 15,
        "thumbnail_url": "/assets/courses/cyber-linux.png",
        "modules": [
            {
                "id": "mod-cyber-3-1",
                "title": "Module 1: Linux Permissions & Privilege Escalation",
                "description": "Octal permissions, SUID/SGID exploitation, sudoers misconfigurations, and PAM modules.",
                "order": 1,
                "lesson_ids": ["cyber-linux-permissions-suid", "cyber-ssh-hardening-bastions"]
            }
        ]
    },
    {
        "id": "course-cyber-lvl4",
        "title": "Cybersecurity Level 4: Web Application Security & OWASP Top 10",
        "slug": "cybersecurity-level-4-web-owasp",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "SQL Injection, Cross-Site Scripting (XSS), CSRF, SSRF, Broken Object Level Auth (BOLA), and PortSwigger mitigation strategies.",
        "category": "Web App Security & OWASP",
        "level": "advanced",
        "estimated_hours": 20,
        "thumbnail_url": "/assets/courses/cyber-owasp.png",
        "modules": [
            {
                "id": "mod-cyber-4-1",
                "title": "Module 1: Injection Attacks & Parameterized Defense",
                "description": "SQLi, Command Injection, second-order injections, and prepared statement parameterization.",
                "order": 1,
                "lesson_ids": ["cyber-sqli-defense-prepared-statements", "cyber-xss-csrf-mitigation"]
            },
            {
                "id": "mod-cyber-4-2",
                "title": "Module 2: Broken Access Control & JWT Vulnerabilities",
                "description": "IDOR, JWT alg=none attacks, missing signature verification, and SSRF mitigations.",
                "order": 2,
                "lesson_ids": ["cyber-jwt-attacks-signature-tampering", "cyber-ssrf-broken-access-control"]
            }
        ]
    },
    {
        "id": "course-cyber-lvl5",
        "title": "Cybersecurity Level 5: Defensive Operations, SIEM & Incident Response",
        "slug": "cybersecurity-level-5-defensive-siem",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "Security Operations Center (SOC) workflows, SIEM rule writing (Splunk/Elastic), Intrusion Detection (Snort/Suricata), and memory forensics.",
        "category": "Threat Hunting & Zero Trust",
        "level": "advanced",
        "estimated_hours": 22,
        "thumbnail_url": "/assets/courses/cyber-defense.png",
        "modules": [
            {
                "id": "mod-cyber-5-1",
                "title": "Module 1: SIEM Log Ingestion & Threat Hunting",
                "description": "Log normalization, correlation rules, IDS signature crafting, and MITRE ATT&CK mapping.",
                "order": 1,
                "lesson_ids": ["cyber-siem-log-correlation-mitre", "cyber-incident-response-digital-forensics"]
            }
        ]
    },
    {
        "id": "course-cyber-lvl6",
        "title": "Cybersecurity Level 6: Advanced Security, Cloud & Zero Trust",
        "slug": "cybersecurity-level-6-cloud-zero-trust",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "description": "Cloud security postures (AWS IAM/Kubernetes RBAC), DevSecOps CI/CD scanning, and Enterprise Zero Trust Architecture.",
        "category": "Threat Hunting & Zero Trust",
        "level": "expert",
        "estimated_hours": 24,
        "thumbnail_url": "/assets/courses/cyber-zerotrust.png",
        "modules": [
            {
                "id": "mod-cyber-6-1",
                "title": "Module 1: Cloud & Container Security",
                "description": "Kubernetes container escapes, IAM least-privilege policies, and DevSecOps pipelines.",
                "order": 1,
                "lesson_ids": ["cyber-cloud-container-kubernetes-security", "cyber-zero-trust-architecture-hsm"]
            }
        ]
    }
]

LESSONS_DATA = [
    {
        "id": "cyber-cia-triad-threat-modeling",
        "title": "The CIA Triad & STRIDE Threat Modeling",
        "slug": "cyber-cia-triad-threat-modeling",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl1",
        "order": 1,
        "xp_reward": 50,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Security Architecture: The CIA Triad & STRIDE

Security engineering rests upon three foundational pillars:
1. **Confidentiality**: Ensuring data is inaccessible to unauthorized entities (Encryption, Access Control).
2. **Integrity**: Ensuring data cannot be altered or tampered with undetectably (Hashing, Digital Signatures).
3. **Availability**: Ensuring authorized users have uninterrupted access to resources (Redundancy, DDoS Defense).

### STRIDE Threat Modeling Framework
- **S**poofing: Impersonating identities $\\to$ Authenticate with PKI / MFA.
- **T**ampering: Modifying data in transit/rest $\\to$ Sign with HMAC / SHA-256.
- **R**epudiation: Denying actions $\\to$ Immutable audit logs.
- **I**nformation Disclosure: Exposing confidential data $\\to$ Encrypt with AES-GCM.
- **D**enial of Service: Exhausting resources $\\to$ Rate limiting & CDN caching.
- **E**levation of Privilege: Gaining unauthorized access $\\to$ Principle of Least Privilege.
"""
    },
    {
        "id": "cyber-auth-authorization-access-control",
        "title": "Authentication, Authorization & RBAC/ABAC Models",
        "slug": "cyber-auth-authorization-access-control",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl1",
        "order": 2,
        "xp_reward": 55,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Authentication vs Authorization

- **Authentication (AuthN)**: "Who are you?" (Passwords + Argon2, FIDO2 WebAuthn, OAuth 2.0).
- **Authorization (AuthZ)**: "What are you permitted to do?" (Role-Based Access Control - RBAC, Attribute-Based Access Control - ABAC).
"""
    },
    {
        "id": "cyber-symmetric-asymmetric-encryption",
        "title": "AES-GCM & RSA/ECC Public Key Cryptography",
        "slug": "cyber-symmetric-asymmetric-encryption",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl1",
        "order": 3,
        "xp_reward": 65,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Applied Cryptography: Symmetric vs Asymmetric

### 1. Symmetric Encryption: AES-256-GCM
Uses a single shared key for high-throughput authenticated encryption with associated data (AEAD):
$$C, T = \\text{AES-GCM}(K, \\text{Nonce}, P, \\text{AAD})$$

### 2. Asymmetric Cryptography: RSA & Elliptic Curves
RSA is founded on the computational hardness of factoring the product of two large prime numbers $N = p \\cdot q$:
- Public Key: $(e, N)$
- Private Key: $(d, N)$ where $e \\cdot d \\equiv 1 \\pmod{\\phi(N)}$
"""
    },
    {
        "id": "cyber-sha256-hashing-digital-signatures",
        "title": "SHA-256 Hashing, Avalanche Effect & Digital Signatures",
        "slug": "cyber-sha256-hashing-digital-signatures",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl1",
        "order": 4,
        "xp_reward": 65,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Cryptographic Hashing & The Avalanche Effect

A cryptographic hash function $H(M) \\to \\{0, 1\\}^{256}$ satisfies:
1. **Pre-image Resistance (One-way)**: Given $h$, computationally infeasible to find $M$.
2. **Second Pre-image Resistance**: Given $M_1$, infeasible to find $M_2 \\ne M_1$ s.t. $H(M_1) = H(M_2)$.
3. **Collision Resistance**: Infeasible to find any pair $(M_1, M_2)$ s.t. $H(M_1) = H(M_2)$.
4. **Avalanche Effect**: Changing 1 bit in input alters $\\approx 50\\%$ of output bits unpredictably.
"""
    },
    {
        "id": "cyber-tcp-handshake-syn-floods",
        "title": "TCP 3-Way Handshake & SYN Flood Defense",
        "slug": "cyber-tcp-handshake-syn-floods",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl2",
        "order": 1,
        "xp_reward": 60,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# TCP Handshake & SYN Cookies Defense

### The Handshake Sequence:
1. Client $\\to$ Server: `SYN` (Seq = $x$)
2. Server $\\to$ Client: `SYN-ACK` (Seq = $y$, Ack = $x+1$)
3. Client $\\to$ Server: `ACK` (Ack = $y+1$)

### SYN Flood Attack & SYN Cookies
In a SYN flood, an attacker sends thousands of spoofed `SYN` packets without completing step 3, filling the server's backlog queue.
**SYN Cookies** encode state into the server's initial sequence number $y = \\text{Hash}(S_{\\text{IP}}, D_{\\text{IP}}, S_{\\text{port}}, D_{\\text{port}}, \\text{secret})$, eliminating the need to allocate memory until the final `ACK` arrives.
"""
    },
    {
        "id": "cyber-dns-arp-spoofing-attacks",
        "title": "ARP Poisoning, MITM & DNS Spoofing",
        "slug": "cyber-dns-arp-spoofing-attacks",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl2",
        "order": 2,
        "xp_reward": 65,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Layer 2 & 3 Spoofing Attacks

- **ARP Poisoning**: Sending unsolicited gratuitous ARP replies mapping the default gateway IP to the attacker's MAC address, routing subnet traffic through the attacker.
- **Defense**: Dynamic ARP Inspection (DAI) and static ARP tables.
"""
    },
    {
        "id": "cyber-nmap-port-scanning-firewalls",
        "title": "Nmap Scanning Techniques & Stateful Firewalls",
        "slug": "cyber-nmap-port-scanning-firewalls",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl2",
        "order": 3,
        "xp_reward": 70,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Port Scanning & Firewall Rules

- **TCP Connect Scan (`-sT`)**: Completes full 3-way handshake (logged by OS).
- **SYN Stealth Scan (`-sS`)**: Sends `SYN`, listens for `SYN-ACK`, immediately sends `RST` to avoid opening a full connection.
- **Stateful Packet Inspection (SPI)**: Tracks `ESTABLISHED,RELATED` connection tables (iptables/nftables).
"""
    },
    {
        "id": "cyber-wireshark-packet-analysis",
        "title": "Wireshark PCAP Inspection & TLS Decryption",
        "slug": "cyber-wireshark-packet-analysis",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl2",
        "order": 4,
        "xp_reward": 75,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Deep Packet Inspection with Wireshark

Filtering syntax:
```text
http.request.method == "POST" || tcp.flags.syn == 1 && tcp.flags.ack == 0
```
"""
    },
    {
        "id": "cyber-linux-permissions-suid",
        "title": "Linux Security: Octal Permissions & SUID Exploits",
        "slug": "cyber-linux-permissions-suid",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl3",
        "order": 1,
        "xp_reward": 65,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Linux Security: DAC & SUID Hardening

Permissions bitmask: `rwxrwxrwx` (User, Group, Others).
**SUID (Set Owner User ID)**: When set on an executable (`chmod u+s /bin/binary`), the process executes with the privileges of the file owner (e.g. `root`), creating privilege escalation risks if misconfigured (GTFOBins).
"""
    },
    {
        "id": "cyber-ssh-hardening-bastions",
        "title": "SSH Hardening, Bastion Hosts & Key Exchange",
        "slug": "cyber-ssh-hardening-bastions",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl3",
        "order": 2,
        "xp_reward": 70,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# SSH Server Hardening (/etc/ssh/sshd_config)

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
AllowUsers engineer
```
"""
    },
    {
        "id": "cyber-sqli-defense-prepared-statements",
        "title": "SQL Injection Mechanics & Prepared Statements",
        "slug": "cyber-sqli-defense-prepared-statements",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl4",
        "order": 1,
        "xp_reward": 80,
        "visual_diagram_type": "sql_injection_defense",
        "content": """# OWASP #1: SQL Injection & Mitigation

When untrusted input is interpolated into dynamic SQL strings:
```python
# VULNERABLE:
query = f"SELECT * FROM accounts WHERE user = '{user_input}'"

# SECURE (Prepared Statement):
cursor.execute("SELECT * FROM accounts WHERE user = %s", (user_input,))
```
Prepared statements pre-compile the SQL execution tree, ensuring parameters are treated solely as literal string constants.
"""
    },
    {
        "id": "cyber-xss-csrf-mitigation",
        "title": "XSS (Stored/Reflected), CSP & CSRF Tokens",
        "slug": "cyber-xss-csrf-mitigation",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl4",
        "order": 2,
        "xp_reward": 80,
        "visual_diagram_type": "sql_injection_defense",
        "content": """# Cross-Site Scripting (XSS) & CSRF Defense

- **XSS**: Attacker injects malicious JavaScript into browser contexts.
  - **Defense**: Context-aware output encoding, React JSX escaping, and Content Security Policy (`Content-Security-Policy: default-src 'self'`).
- **CSRF**: Forcing authenticated users to execute unwanted actions.
  - **Defense**: `SameSite=Lax/Strict` cookies and anti-CSRF token headers.
"""
    },
    {
        "id": "cyber-jwt-attacks-signature-tampering",
        "title": "JWT Security: Signature Verification & Key Confusion",
        "slug": "cyber-jwt-attacks-signature-tampering",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl4",
        "order": 3,
        "xp_reward": 85,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# JWT Vulnerabilities & Hardening

A JSON Web Token has three base64url segments: `header.payload.signature`.
Vulnerabilities:
1. `alg=none` exploit: Attacker sets header `alg: "none"` and strips signature.
2. RSA to HMAC Key Confusion: Attacker changes `alg: "RS256"` to `"HS256"` and signs with the server's public key as HMAC secret.
"""
    },
    {
        "id": "cyber-ssrf-broken-access-control",
        "title": "Server-Side Request Forgery (SSRF) & IDOR",
        "slug": "cyber-ssrf-broken-access-control",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl4",
        "order": 4,
        "xp_reward": 85,
        "visual_diagram_type": "sql_injection_defense",
        "content": """# SSRF & Cloud Metadata Protection

SSRF allows attackers to coerce the backend server into sending requests to internal private addresses (`127.0.0.1`, `169.254.169.254` AWS metadata).
Mitigation: IP whitelisting, disabling HTTP redirects, and AWS IMDSv2 session tokens.
"""
    },
    {
        "id": "cyber-siem-log-correlation-mitre",
        "title": "SIEM Log Ingestion & MITRE ATT&CK Mapping",
        "slug": "cyber-siem-log-correlation-mitre",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl5",
        "order": 1,
        "xp_reward": 85,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# SIEM Operations & Threat Intelligence

Mapping anomalous event logs across Tactics, Techniques, and Procedures (TTPs) using the MITRE ATT&CK framework.
"""
    },
    {
        "id": "cyber-incident-response-digital-forensics",
        "title": "Incident Response Lifecycle & Memory Forensics",
        "slug": "cyber-incident-response-digital-forensics",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl5",
        "order": 2,
        "xp_reward": 90,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# NIST Incident Response Framework

1. Preparation
2. Detection & Analysis
3. Containment, Eradication & Recovery
4. Post-Incident Activity (Lessons Learned)
"""
    },
    {
        "id": "cyber-cloud-container-kubernetes-security",
        "title": "Container Security, Kubernetes RBAC & Escape Mitigations",
        "slug": "cyber-cloud-container-kubernetes-security",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl6",
        "order": 1,
        "xp_reward": 95,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Docker & Kubernetes Hardening

- Disallowing `privileged: true` containers
- Read-only root filesystems
- Dropping Linux capabilities (`cap_drop: ALL`)
- NetworkPolicies isolating pod-to-pod traffic
"""
    },
    {
        "id": "cyber-zero-trust-architecture-hsm",
        "title": "Enterprise Zero Trust Architecture & Hardware Security (HSM)",
        "slug": "cyber-zero-trust-architecture-hsm",
        "domain": "cybersecurity",
        "color": "#14B8A6",
        "icon": "ShieldCheck",
        "is_published": True,
        "skills_taught": ['Security Architecture', 'OWASP Top 10', 'Applied Cryptography', 'Zero Trust'],
        "course_id": "course-cyber-lvl6",
        "order": 2,
        "xp_reward": 100,
        "visual_diagram_type": "rsa_crypto_flow",
        "content": """# Zero Trust Principles (NIST SP 800-207)

"Never trust, always verify."
1. Continuous dynamic authentication and authorization for every access request.
2. Microsegmentation of networks.
3. Cryptographic hardware isolation via Hardware Security Modules (HSM) and TPM chips.
"""
    }
]

QUIZZES_DATA = [
    {
        "id": "quiz-cyber-lvl1",
        "lesson_id": "cyber-cia-triad-threat-modeling",
        "title": "Cybersecurity Foundations & Cryptography Diagnostic",
        "passing_score": 80,
        "questions": [
            {
                "id": "q-cyber-1-1",
                "question": "Which cryptographic primitive guarantees both integrity and non-repudiation?",
                "options": ["Symmetric AES-256", "Digital Signatures with Private Key", "Unsalted MD5", "Base64 Encoding"],
                "correct_option_index": 1,
                "explanation": "Digital signatures signed with the private key provide mathematical proof that the message came from the keyholder (non-repudiation) and was not modified in transit (integrity)."
            },
            {
                "id": "q-cyber-1-2",
                "question": "How do prepared statements fundamentally defeat SQL Injection?",
                "options": [
                    "By replacing all quotes with empty strings",
                    "By pre-compiling the SQL query structure before binding user input as strict data literals",
                    "By running the query in an isolated Docker container",
                    "By encoding the query with AES"
                ],
                "correct_option_index": 1,
                "explanation": "Because the query template is compiled into an execution tree prior to parameter insertion, user input is never interpreted as executable SQL syntax."
            }
        ]
    }
]

SKILLS_DATA = [
    {
        "id": "skill-cyber-foundations",
        "name": "Security Foundations & Cryptography",
        "category": "Applied Cryptography",
        "level": 1,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": [],
        "description": "Master CIA Triad, STRIDE threat modeling, AES-GCM, and SHA-256."
    },
    {
        "id": "skill-cyber-owasp-network",
        "name": "Network Security & OWASP Defense",
        "category": "Web App Security & OWASP",
        "level": 2,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-cyber-foundations"],
        "description": "Master SQLi, XSS, CSRF, JWT tampering, and Nmap/Wireshark packet defense."
    },
    {
        "id": "skill-cyber-advanced-zerotrust",
        "name": "Defensive Operations & Zero Trust",
        "category": "Threat Hunting & Zero Trust",
        "level": 3,
        "unlocked": True,
        "progress": 0.0,
        "prerequisites": ["skill-cyber-owasp-network"],
        "description": "Master SIEM correlation, container isolation, and Zero Trust Architecture."
    }
]
