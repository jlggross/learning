/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Qual a média salarial nessa empresa?
*/
select AVG(salario) from empregado

/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Quantos empregados do departamento 5 trabalham mais de 10h por semana no projeto chamado "ProductX"?
*/
SELECT COUNT(*) FROM empregado, trabalha_em, projeto
WHERE empregado.ssn = trabalha_em.essn 
	AND empregado.dno = 5 
	AND projeto.pjnome = 'ProductX'
    and projeto.pnumero = trabalha_em.pno
    AND trabalha_em.horas > 10
	
/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Quantos empregados possuem um dependente com o mesmo primeiro nome que o deles?
*/
SELECT count(*) FROM dependente, empregado
WHERE dependente.essn = empregado.ssn 
	AND dependente.nome_dependente = empregado.pnome
	
/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Quais os nomes de todos os empregados que são diretamente supervisionados por Franklin Wong
*/
SELECT empregado.PNOME FROM empregado 
WHERE empregado.superssn = '333445555'

/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Quem é a pessoa que possui mais tempo de alocação no projeto 'Newbenefits'?
*/
SELECT empregado.pnome, trabalha_em.horas FROM empregado, trabalha_em, projeto
WHERE empregado.ssn = trabalha_em.essn 
	AND projeto.pjnome = 'Newbenefits'
    and projeto.pnumero = trabalha_em.pno
ORDER by trabalha_em.horas desc

/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Qual é a soma dos salários de todos os empregados do departamento chamado 'Research'?
*/
SELECT sum(empregado.salario) FROM departamento, empregado
WHERE departamento.dnome = 'Research'
	AND departamento.dnumero = empregado.dno

/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Qual seria o custo do projeto com folha salarial (soma de todos os salários) caso a empresa desse 10% de aumento para todos os empregados que trabalham no projeto 'ProductX'?
*/
SELECT sum(empregado.salario)*1.1 FROM projeto, empregado, trabalha_em
WHERE projeto.pjnome = 'ProductX'
	AND projeto.pnumero = trabalha_em.pno
    AND trabalha_em.essn = empregado.ssn

/*
Considere o banco de dados do enunciado. Crie uma consulta em SQL e responda: Qual o nome do departamento com a menor média de salário entre seus funcionários?
*/
SELECT departamento.dnome,AVG(empregado.salario) FROM empregado, departamento
WHERE empregado.dno = departamento.dnumero
group by departamento.dnumero
order by AVG(empregado.salario) 


