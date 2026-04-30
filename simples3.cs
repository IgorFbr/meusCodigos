using UnityEngine;

public class desafioifelse : MonoBehaviour
{
   
    public int numero_1;
    public int numero_2;
    public int numero_3;
    public int numero_maior;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        if (numero_1 > numero_maior)
            Debug.Log(" numero 1 é maior que o numero maior");
        else if (numero_2 > numero_maior)
            Debug.Log("numero 2 é maior");
        else if (numero_3 > numero_maior)
            Debug.Log("numeor 3 é maior");
        else
        {
            Debug.Log(" o numero maior é maior");
        }


    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
