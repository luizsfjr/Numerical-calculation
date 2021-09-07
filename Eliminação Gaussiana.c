#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{
    int ordem;
    int i, j, k, z, y;

    printf("Digite a ordem do sistema: ");
    scanf("%d", &ordem);
    double coef[ordem][ordem], res[ordem], sol[ordem];

    /* Leitura dos coeficientes e resultados
        das equações*/
    for(i = 0; i < ordem; i++){
        for(j = 0; j < ordem; j++){
            scanf("%lf", &coef[i][j]);
        }
        printf("Resultado equacao %d: ", i+1);
        scanf("%lf", &res[i]);
        printf("\n"); printf("----------\n"); printf("\n");
    }


    for(k = 0; k < ordem-1; k++){
        double maior = fabs(coef[k][k]);
        int maiorIndice = k;

        /*Procura do maior coeficiente presente
        na coluna k, sendo necessário para minimizar
        erros de arredondamento e divisões por zero.*/
        for(i = k + 1; i < ordem; i++){
            if(maior < fabs(coef[i][k])){
                maior = fabs(coef[i][k]);
                maiorIndice = i;
            }
        }

        //Permutação de equações caso necessário!
        if(maiorIndice != k){
            for(j = 0; j < ordem; j++){
                double aux = coef[k][j];
                coef[k][j] = coef[maiorIndice][j];
                coef[maiorIndice][j] = aux;
            }
            double aux = res[k];
            res[k] = res[maiorIndice];
            res[maiorIndice] = aux;
        }
        if(coef[k][k] == 0){
            printf("Sistema impossivel ou possivel indeterminado!\n");
        }else{
            for(z = k + 1; z < ordem; z++){
                double fator = -coef[z][k] /coef[k][k];
                coef[z][k] = 0;
                res[z] = res[z] + fator*res[k];
                for(y = k + 1; y < ordem; y++){
                    coef[z][y] = coef[z][y] + fator*coef[k][y];
                }
            }
        }

    }

    /* Resolução do sistema triangular superior
    equivalente à equação original*/
    for(i = ordem - 1; i >= 0; i--){
        sol[i] = res[i];
        for(j = i + 1; j < ordem; j++){
            sol[i] = sol[i] - sol[j]*coef[i][j];
        }
        sol[i] = sol[i]/coef[i][i];
    }

    // Matriz pós aplicação do método de gauss.
    for(i = 0; i < ordem; i++){
            for(j = 0; j < ordem; j++){
                printf("%.2lf\t", coef[i][j]);
            }
            printf("res -> %.2f", res[i]);
            printf("\n");
    }

    //Exibição das soluções
    printf("\n");
    printf("Soluções:\n");
    printf("\n");
    for(i = 0; i < ordem; i++){
        printf("x%d = %.2lf\n", i+1, sol[i]);
    }
    return 0;
}
