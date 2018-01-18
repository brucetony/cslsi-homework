# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:39:44 2018

@author: Bruce
"""

import numpy as np
import random

a = np.array([[3, 1], [4, 3]])
c = np.array([[2, 1.5], [0, 3]])

testa = np.array([[0.70000, 0.70711], [0.70001, 0.70711]])
testq = np.array([[0.70710, 1.0000], [0.70711, 0]])
testr = np.array([[0.98996, 1.0000]])

#a.)
def proj(u, v):
    '''
    Function that return the projection of v onto u
    '''
    return u*(np.dot(u, v)/np.dot(u, u))

def CGS(A):
    '''
    Function using classical Gram-Schmidt Algorithm and returns Q and R
    matrices.
    '''
    
    R = np.zeros((len(A), len(A))) #Empty coefficient list
    Q = np.zeros(np.shape(A)) #Empty Q matrix, same dim as input matrix
    for j in range(len(A)): #For each vector in A
        matrix_vec = A[:,j] # Define our vector
        for i in range(j):
            R[i, j] = np.dot(np.transpose(Q[i]), A[:,j])
            matrix_vec = matrix_vec - R[i, j]*Q[:,i]
        R[j, j] = np.linalg.norm(matrix_vec)
        Q[:,j] = matrix_vec/R[j, j] #Insert orthonormal vec in Q matrix
    
    return Q, R
    
def MGS(A):
    '''
    Uses modified Gram-Schmidt algorithm to generate Q and R matrices from
    input A matrix
    '''
    R = np.zeros((len(A), len(A))) #Empty coefficient list
    Q = np.zeros(np.shape(A)) #Empty Q matrix, same dim as input matrix
    for j in range(len(A)): #For each vector in A
        matrix_vec = A[:,j] # Define our vector
        for i in range(j):
            R[i, j] = np.dot(np.transpose(Q[i]), matrix_vec)
            matrix_vec = matrix_vec - R[i, j]*Q[:,i]
        R[j, j] = np.linalg.norm(matrix_vec)
        Q[:,j] = matrix_vec/R[j, j] #Insert orthonormal vec in Q matrix
    
    return Q, R

def Householder(A):
    '''
    I do not think this is correctly done
    '''
    m, n = np.shape(A)
    R = np.copy(A)
    Qt = np.eye(A.shape[0])
    for k in range(n):
        matrix_vec = np.copy(R[k:,k])
        basis_vec = np.zeros(len(matrix_vec)) #Standard basis vector
        basis_vec[0] = 1 #Replace 0 with 1 are index position
        sign = np.sign(matrix_vec[0])
        ortho_vec = sign*np.linalg.norm(matrix_vec)*basis_vec+matrix_vec
        ortho_vec = ortho_vec/np.linalg.norm(ortho_vec) #Normalize vector
        difference = 2*np.dot(np.outer(ortho_vec,ortho_vec),(R[k:,k:])) #Maybe outer product?
        R[k:,k:] = R[k:,k:] - difference
        
        #End Householder algorithm and now get Q
        Qt[k:, k:] = Qt[k:, k:] - 2*np.dot(np.outer(ortho_vec,ortho_vec),(Qt[k:,k:]))
    Qt = np.transpose(Qt)
        
    return Qt, R

#b.)
def QRerror(A, Q, R):
    m, n = np.shape(A)
    q_row, q_col = np.shape(Q)
    qr_values = []
    ortho_values = []
    
    qr_diff = A-Q*R
    for i in range(m):
        for j in range(n):
            qr_values.append((qr_diff[i, j])**2)
    qr_error = sum(qr_values)**0.5
    
    I = np.identity(q_row)
    ortho_diff = np.transpose(Q)*Q-I
    for g in range(q_row):
        for h in range(q_col):
            ortho_values.append((ortho_diff[i, j])**2)
    ortho_error = sum(ortho_values)**0.5
       
    return qr_error, ortho_error

#HouseholderR(c)
#print(c)
#print(np.linalg.qr(a, mode='r'))

#c.)   
#Single Precision Floating Point Test
#testa = np.float32(testa)
#cgs_sing_q, cgs_sing_r = CGS(testa)
#mgs_sing_q, mgs_sing_r = MGS(testa)
#hh_sing_sing_q, hh_sing_sing_r = Householder(testa)
#cgs_sing_fac_error, cgs_sing_ortho = QRerror(testa, cgs_sing_q, cgs_sing_r)
#mgs_sing_fac_error, mgs_sing_ortho = QRerror(testa, mgs_sing_q, mgs_sing_r)
#hh_sing_fac_error, hh_sing_ortho = QRerror(testa, hh_sing_sing_q, hh_sing_sing_r)
#
#print("Single - CGS - Factorization Error = ", cgs_sing_fac_error)
#print("Single - MGS - Factorization Error = ", mgs_sing_fac_error)
#print("Single - Householder - Factorization Error = ", hh_sing_fac_error)
#
##Double Precision Floating Point Test
#testa = np.float64(testa)
#cgs_doub_q, cgs_doub_r = CGS(testa)
#mgs_doub_q, mgs_doub_r = MGS(testa)
#hh_doub_sing_q, hh_doub_sing_r = Householder(testa)
#cgs_doub_fac_error, cgs_doub_ortho = QRerror(testa, cgs_doub_q, cgs_doub_r)
#mgs_doub_fac_error, mgs_doub_ortho = QRerror(testa, mgs_doub_q, mgs_doub_r)
#hh_doub_fac_error, hh_doub_ortho = QRerror(testa, hh_doub_sing_q, hh_doub_sing_r)
#
#print("Double - CGS - Factorization Error = ", cgs_doub_fac_error)
#print("Double - MGS - Factorization Error = ", mgs_doub_fac_error)
#print("Double - Householder - Factorization Error = ", hh_doub_fac_error)
# ORtho
#print("Single - CGS - Orthoganality Error = ", cgs_sing_ortho)
#print("Single - MGS - Orthoganality Error = ", mgs_sing_ortho)
#print("Single - Householder - Orthoganality Error = ", hh_sing_ortho)
#print("Double - CGS - Orthoganality Error = ", cgs_doub_ortho)
#print("Double - MGS - Orthoganality Error = ", mgs_doub_ortho)
#print("Double - Householder - Orthoganality Error = ", hh_doub_ortho)

#d.)
def buildMatrix(m, n):
    '''
    Create a mxn matrix with random integers
    '''
    A = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            A[i, j] = random.randint(0, 20)
    return A

def diagS(m):
    '''
    Creates a mxm diaaonal matrix with values 2^(-i) for i 1:m
    '''
    S = np.zeros((m, m))
    for i in range(m):
        S[i, i] = 2**(-(i+1))
    return S

#U, R = (np.linalg.qr(buildMatrix(80, 80)))
#V, R = (np.linalg.qr(buildMatrix(80, 80)))
#S = diagS(80)
#M = U*S*V
#N = np.float32(np.copy(M)) #Single
#
##Single Precision
#cgs_n_q, cgs_n_r = CGS(N)
#mgs_n_q, mgs_n_r = MGS(N)
#hh_n_q, hh_n_r = Householder(N)
#cgs_n_fac_error, cgs_n_ortho = QRerror(N, cgs_n_q, cgs_n_r)
#mgs_n_fac_error, mgs_n_ortho = QRerror(N, mgs_n_q, mgs_n_r)
#hh_n_fac_error, hh_n_ortho = QRerror(N, hh_n_q, hh_n_r)
#
#print("Single - CGS - Factorization Error = ", cgs_n_fac_error)
#print("Single - MGS - Factorization Error = ", mgs_n_fac_error)
#print("Single - Householder - Factorization Error = ", hh_n_fac_error)
#
##Double Precision
#cgs_m_q, cgs_m_r = CGS(M)
#mgs_m_q, mgs_m_r = MGS(M)
#hh_m_q, hh_m_r = Householder(M)
#cgs_m_fac_error, cgs_m_ortho = QRerror(N, cgs_m_q, cgs_m_r)
#mgs_m_fac_error, mgs_m_ortho = QRerror(N, mgs_m_q, mgs_m_r)
#hh_m_fac_error, hh_m_ortho = QRerror(N, hh_m_q, hh_m_r)
#
#print("Double - CGS - Factorization Error = ", cgs_m_fac_error)
#print("Double - MGS - Factorization Error = ", mgs_m_fac_error)
#print("Double - Householder - Factorization Error = ", hh_m_fac_error)
##Ortho
#print("Single - CGS - Orthoganality Error = ", cgs_n_ortho)
#print("Single - MGS - Orthoganality Error = ", mgs_n_ortho)
#print("Single - Householder - Orthoganality Error = ", hh_n_ortho)
#print("Double - CGS - Orthoganality Error = ", cgs_m_ortho)
#print("Double - MGS - Orthoganality Error = ", mgs_m_ortho)
#print("Double - Householder - Orthoganality Error = ", hh_m_ortho)
