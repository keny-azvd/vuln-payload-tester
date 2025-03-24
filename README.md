# vuln-payload-tester
A Python script designed to test web applications for vulnerabilities by sending various payloads to identify potential Server-Side Template Injection (SSTI) vulnerabilities. The tool allows you to input base URLs and paths, then posts crafted payloads to evaluate the server's response and highlight potential weaknesses.


# vuln-payload-tester

**vuln-payload-tester** is a Python-based tool designed to help security researchers and developers identify Server-Side Template Injection (SSTI) vulnerabilities in web applications. The tool works by sending crafted payloads to the server and analyzing the responses to detect possible code execution or data leaks caused by improperly handled user inputs in templates.

## Table of Contents

- [Overview](#overview)



## Overview

Server-Side Template Injection (SSTI) occurs when an attacker can inject malicious code into the server-side template engine, leading to remote code execution or data leakage. SSTI vulnerabilities can be exploited in many popular web frameworks that use templating engines, such as Jinja2, Twig, and Velocity.

The **vuln-payload-tester** automates the process of testing for SSTI vulnerabilities by posting various payloads to specified paths on a target web application and analyzing the responses.



